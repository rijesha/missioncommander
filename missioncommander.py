from gi.repository import Gtk

import threading
import gui
import ivylinker
import test
import interopclient
import time
from time import clock
import pyproj


class main:
    def __init__( self ):
        self.newmissionstatus = False
        self.lastmissionmsg = None
        self.lastgps = None
        self.lastattitude = None
        self.lastestimator = None
        self.telinfoavailable = False
        self.shutdown = False
        self.initIVY()
        self.initGUI()
        self.initINTEROP()
        self.interopTH = threading.Thread(target = self.interophandler)
        self.interopTH.start()
        self.guihandler()
#        self.guiTH = threading.Thread(target = self.guihandler)
#        self.guiTH.start()
        print("SDFDSKFJDSLJFLKDSFKLDSFKJLSDJKLFJKDSFKLDSJKFJDSKL")

    def shutdownprog(self):
        self.ivylink.shutdown()
        self.shutdown = True

    def initIVY( self):
        self.ivylink = ivylinker.CommandSender(verbose=True, callback = self.msg_handler)
        self.lastmissionmessagetime = clock()

    def msg_handler(self, acid, msg):
        if (msg.name == "MISSION_STATUS" and (self.lastmissionmessagetime + .02) < (clock())):
            self.lastmissionmsg = msg
            self.newmissionstatus = True
            self.lastmissionmessagetime = clock()

        if (msg.name == "GPS"):
            self.lastgps = msg

        if (msg.name == "ATTITUDE"):
            self.lastattitude = msg

        if (msg.name == "ESTIMATOR"):
            self.lastestimator = msg

        if (self.lastgps != None) and (self.lastattitude != None) and (self.lastestimator != None):
            self.telinfoavailable = True




    def initGUI( self):
        print("initiiaaaliesdfsdaiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
        self.win = gui.MissionGUI(shutdowncb = self.shutdownprog)
        self.win.window.show_all()
        self.win.ivybind(self.ivylink)
        self.i =1

    def guihandler(self):
        print("runnnnnnnnnnnnnnnnnnnning")
        i=1
        while self.shutdown==False:
            if self.newmissionstatus == True:
                self.win.update_uav_queue(self.lastmissionmsg)
                self.newmissionstatus = False
            elif Gtk.events_pending():
                i=i+1
                print(i)
                Gtk.main_iteration()
            time.sleep(0.02)

    def initINTEROP(self):
        self.interoplink = interopclient.Connection()
        self.lastmoveobjecttime = clock()-10
        self.laststationojecttime = clock()-10
        self.bypassinghashtable = 0
        self.bypassinghashtable1 = 0
        self.lastupdatetelemetry = clock()-10

    def interophandler(self):
        while True:
            if self.lastmoveobjecttime + .01 < clock():
                self.movinghandler()
                self.lastmoveobjecttime = clock()

            if self.laststationojecttime + .1 < clock():
                self.stationaryhandler()
                self.laststationojecttime = clock()

            if self.lastupdatetelemetry + .01 <clock() and self.telinfoavailable :
                print("updating telemetr")
                self.telemetryhandler()
                self.lastupdatetelemetry = clock()

            if self.shutdown == True:
                return 0
            time.sleep(0.02)


    def stationaryhandler(self):
        objects = self.interoplink.getobstacleinfo()
        station = objects.get("stationary_obstacles")
        #need to generate some sort of hash table to index moving objects
        i =2
        for ob in station:
            if self.bypassinghashtable1 ==0:
                self.ivylink.add_obstacle_dict("create",i, ob)
                i=i+1
        self.bypassinghashtable1 = 1

    def movinghandler(self):
        objects = self.interoplink.getobstacleinfo()
        moving = objects.get("moving_obstacles")
        #need to generate some sort of hash table to index moving objects
        #if object already exits in hashtable then update else creat, add to hastable then update
        for ob in moving:
            if self.bypassinghashtable == 1:
                self.ivylink.add_obstacle_dict("update",1, ob)
                print(type(ob.get("longitude")))
            else:
                self.bypassinghashtable = 1
                print(ob.get("longitude"))
                self.ivylink.add_obstacle_dict("create",1, ob)

    def telemetryhandler(self):
        lat, lon = self.utm_to_DD((self.lastgps.fieldvalues[1]), ( self.lastgps.fieldvalues[2] ), self.lastgps.fieldvalues[9])
        alt = self.lastestimator.fieldvalues[0]
        course = float(self.lastattitude.fieldvalues[1]) * 180 / 3.14
        tele = {'latitude':float(lat), 'longitude':float(lon), 'altitude_msl':float(alt), 'uas_heading':course}
        self.interoplink.updatetelemetry(tele)


    def utm_to_DD(self, easting, northing, zone, hemisphere="northern"):
        """
        Converts a set of UTM GPS coordinates to WGS84 Decimal Degree GPS coordinates.
        Returns (latitude, longitude) as a tuple.
        easting - UTM easting in metres
        northing - UTM northing in metres
        zone - current UTM zone

        Note that no hemisphere is specified; in the southern hemisphere, this function expects the false northing (10 000 000m) to be subtracted.

        An exception will be raised if the conversion involves invalid values.
        """

        easting = float(easting) / 100
        northing =  float(northing) / 100
        zone = int(zone)
        # Easting and Northing ranges from https://www.e-education.psu.edu/natureofgeoinfo/c2_p23.html
        min_easting, max_easting = 167000, 833000
        if not (min_easting < easting < max_easting):
            print("prinsgfjadslkfjsfdsprint")
            print(easting)
            raise(ValueError("Easting value of %s is out of bounds (%s to %s)." % (easting, min_easting, max_easting)))
        min_northing, max_northing = -9900000, 9400000
        if not (min_northing < northing < max_northing):
            raise(ValueError("Northing value of %s is out of bounds (%s to %s)." % (northing, min_northing, max_northing)))

        if not (1 <= zone <= 60):
            raise(ValueError("Zone value of %s is out of bounds" % zone))

        pr = pyproj.Proj(proj='utm', zone=zone, ellps='WGS84', errcheck=True)

        lon, lat = pr(easting, northing, inverse=True)
        return repr(lat), repr(lon)

if __name__ == "__main__":
    main()
