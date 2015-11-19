from gi.repository import Gtk

import threading
import gui
import ivylinker
import test
from time import clock

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

    def ivyGUI(self, ivy):
        self.win.ivybind(ivy.link)
        

def shutdown():
    ivy.link.shutdown()

if __name__ == "__main__":
    UI = GUIbinder(shutdown)
    ivy = ivyInit(UI)
    UI.ivyGUI(ivy)
    Gtk.main()



