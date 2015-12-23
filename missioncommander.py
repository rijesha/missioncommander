from gi.repository import Gtk

import threading
import gui
import ivylinker
import test
import interopclient
import time
from time import clock


class main:
    def __init__( self ):
        self.newmissionstatus = False
        self.lastmissionmsg = None
        self.shutdowngui = False
        self.initIVY()
        self.initGUI()
        self.initINTEROP()
        self.interopTH = threading.Thread(target = self.interophandler)
        self.interopTH.start()
        self.guihandler()
#        self.guiTH = threading.Thread(target = self.guihandler)
#        self.guiTH.start()
        print("SDFDSKFJDSLJFLKDSFKLDSFKJLSDJKLFJKDSFKLDSJKFJDSKL")

    def shutdown(self):
        self.ivylink.shutdown()
        self.shutdowngui = True

    def initIVY( self):
        self.ivylink = ivylinker.CommandSender(verbose=True, callback = self.msg_handler)
        self.lastmissionmessagetime = clock()

    def msg_handler(self, acid, msg):
        if (msg.name == "MISSION_STATUS" and (self.lastmissionmessagetime + .02) < (clock())):
            self.lastmissionmsg = msg
            self.newmissionstatus = True
            self.lastmissionmessagetime = clock()

    def initGUI( self):
        print("initiiaaaliesdfsdaiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
        self.win = gui.MissionGUI(shutdowncb = self.shutdown)
        self.win.window.show_all()
        self.win.ivybind(self.ivylink)
        self.i =1

    def guihandler(self):
        print("runnnnnnnnnnnnnnnnnnnning")
        i=1
        #Gtk.main()
        while self.shutdowngui==False:
            if self.newmissionstatus == True:
                self.win.update_uav_queue(self.lastmissionmsg)
                self.newmissionstatus = False
            elif Gtk.events_pending():
                i=i+1
                print(i)
                Gtk.main_iteration()

            time.sleep(0.01)

    def initINTEROP(self):
        self.interoplink = interopclient.Connection()
        self.lastmoveobjecttime = clock()-.01
        self.laststationojecttime = clock()-.1
        self.bypassinghashtable = 0
        self.bypassinghashtable1 = 0

    def interophandler(self):
        while True:
            if self.lastmoveobjecttime + .01 < clock():
                print("hey move")
                self.movinghandler()
                self.lastmoveobjecttime = clock()

            if self.laststationojecttime + .1 < clock():
                print("hey 1")
                self.stationaryhandler()
                self.laststationojecttime = clock()

            time.sleep(0.01)

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


if __name__ == "__main__":
    main()
