from gi.repository import Gtk

import threading
import gui
import ivylinker
import test
from time import clock


class main:
    def __init__( self ):
        self.newmissionstatus = False
        self.lastmissionmsg = None
        self.shutdowngui = False
        self.ivy = ivyhandler(parent = self)
        self.UIthread = guihandler(parent = self)

    def shutdown(self):
        self.ivy.link.shutdown()
        self.shutdowngui = True

class ivyhandler:
    def __init__( self, parent=None ):
        self.parent = parent
        self.link = ivylinker.CommandSender(verbose=True, callback = self.msg_handler)
        self.lastmissionmessagetime = clock()

    def msg_handler(self, acid, msg):
        if (msg.name == "MISSION_STATUS" and (self.lastmissionmessagetime + .02) < (clock())):
            self.parent.lastmissionmsg = msg
            self.parent.newmissionstatus = True
            self.lastmissionmessagetime = clock()

class guihandler:
    def __init__( self, parent=None):
        self.win = gui.MissionGUI(shutdowncb = parent.shutdown)
        self.win.window.show_all()
        self.win.ivybind(parent.ivy.link)
        self.i =1
        while parent.shutdowngui==False:
            if parent.newmissionstatus == True:
                self.win.update_uav_queue(parent.lastmissionmsg)
                parent.newmissionstatus = False
            elif Gtk.events_pending():
                Gtk.main_iteration()

if __name__ == "__main__":
    main()
