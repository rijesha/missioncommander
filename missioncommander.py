from gi.repository import Gtk

import threading
import gui
import ivylinker
import test


class ivyInit:
    def __init__( self, UI ):
        self.UI = UI
        self.link = ivylinker.CommandSender(verbose=True, callback = self.msg_handler)

    def msg_handler(self, acid, msg):
        if (msg.name == "MISSION_STATUS"):    
            self.UI.win.update_uav_queue(msg)
        

class GUIstarter:
    def __init__( self, shutdown ):
        self.win = gui.MissionGUI(shutdowncb = shutdown)
        self.win.window.show_all()



def shutdown():
    ivy.link.shutdown()

if __name__ == "__main__":
    UI = GUIstarter(shutdown)
    ivy = ivyInit(UI)
    Gtk.main()

