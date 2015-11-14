from gi.repository import Gtk

import threading
import gui
import ivylinker
import test


class ivyInit:
    def __init__( self ):
        self.link = ivylinker.CommandSender(verbose=True, callback = self.msg_handler)

    def msg_handler(self, acid, msg):
        if (msg.name == "MISSION_STATUS"):
            print(msg)
        

class GUIstarter:
    def __init__( self, shutdown ):
        win = gui.MissionGUI(shutdowncb = shutdown)
        win.window.show_all()
        Gtk.main()




def shutdown():
    ivy.link.shutdown()

if __name__ == "__main__":
    ivy = ivyInit()
    UI = GUIstarter(shutdown)

