#!/usr/local/bin/python

from gi.repository import Gtk
from time import clock
import threading

import interopclient
import gui
import ivylinker



class ivyInit:
    def __init__( self, UI ):
        self.UI = UI
        self.link = ivylinker.CommandSender(verbose=True, callback = self.msg_handler)
        self.lastmissionmessagetime = clock()

    def msg_handler(self, acid, msg):
        if (msg.name == "MISSION_STATUS" and (self.lastmissionmessagetime + .02) < (clock())):           
            self.UI.win.update_uav_queue(msg)
            self.lastmissionmessagetime = clock()

class GUIbinder:
    def __init__( self, shutdown):
        self.win = gui.MissionGUI(shutdowncb = shutdown)
        self.win.window.show_all()

    def passivyintoGUI(self, ivy):
        self.win.ivybind(ivy)
        

class interophandler(threading.Thread):
    def __init__(self, ivylink):
        super(interophandler, self).__init__()
        self.ivylink = ivylink
        self.con = interopclient.Connection()
        self.lastmoveobjecttime = clock()-.7
        self.laststationojecttime = clock()-10
        print("hellsdfO")
        self.bypassinghashtable = 0
        self.bypassinghashtable1 = 0

    
    def run(self):
        while True:
            if self.lastmoveobjecttime + .7 < clock():
                self.movinghandler()
                self.lastmoveobjecttime = clock()  
 
            if self.laststationojecttime + 10 < clock():
                self.stationaryhandler()
                self.laststationojecttime = clock()              
            

    def stationaryhandler(self):
        objects = self.con.getobstacleinfo()
        station = objects.get("stationary_obstacles")
        #need to generate some sort of hash table to index moving objects
        i =2
        for ob in station:
            if self.bypassinghashtable1 ==0:
                self.ivylink.add_obstacle_dict("create",i, ob)
                i=i+1
        self.bypassinghashtable1 = 1

    def movinghandler(self):
        objects = self.con.getobstacleinfo()
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


def shutdown():
    ivy.link.shutdown()

if __name__ == "__main__":
    UI = GUIbinder(shutdown)
    ivy = ivyInit(UI)
    UI.passivyintoGUI(ivy.link)

    #interopTH = threading.Thread(target = interophandler, args = ivy)
    interopTH = interophandler(ivy.link)
    interopTH.daemon = True
    print("hellO")
    interopTH.start()
    Gtk.main()



