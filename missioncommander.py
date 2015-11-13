from gi.repository import Gtk

import threading
import gui
import ivylinker
import test


class guiThread:
    def __init__( self ):
        builder = Gtk.Builder()
        builder.add_from_file( "test.glade" )
        
        self.window = builder.get_object( "window1" )
        self.newcommand = builder.get_object( "dialog1" )
        self.stagingarea = builder.get_object( "stagingarea" )
        self.stagingstore = builder.get_object( "stagingstore" )
        self.archivearea = builder.get_object( "archivearea" )
        self.archivestore = builder.get_object( "archivestore" )

        builder.connect_signals( self )

class ivylinkerThread:
    def __init__( self ):
        builder = Gtk.Builder()
        builder.add_from_file( "test.glade" )
        
        self.window = builder.get_object( "window1" )
        self.newcommand = builder.get_object( "dialog1" )
        self.stagingarea = builder.get_object( "stagingarea" )
        self.stagingstore = builder.get_object( "stagingstore" )
        self.archivearea = builder.get_object( "archivearea" )
        self.archivestore = builder.get_object( "archivestore" )

        builder.connect_signals( self )


if __name__ == "__main__":
    guiTH = threading.Thread(target=gui.GUIstarter)
    ivylsnTH = threading.Thread(target=ivylinker.CommandSender)
    testTH = threading.Thread(target=test.hello)

    guiTH.start()
    ivylsnTH.start()
    testTH.start()
