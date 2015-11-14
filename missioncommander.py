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
        



def shutdown():
    ivy.shutdown()

if __name__ == "__main__":
    ivy = ivyInit()
    UI = gui.GUIstarter()




#    guiTH = threading.Thread(target=gui.GUIstarter)
#    ivylsnTH = threading.Thread(target=ivylinker.CommandSender)
#    testTH = threading.Thread(target=test.hello)

#    guiTH.start()
#    ivylsnTH.start()
#    testTH.start()
