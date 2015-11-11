from gi.repository import Gtk

class Sample:
    def gtk_main_quit( self, window ):
        Gtk.main_quit()

    def sendtostaging_clicked_cb( self, button ):
        select = self.archivearea.get_selection()
        selected_rows = select.get_selected_rows()
        path = selected_rows[1]
        row = path[0]
        index = row.get_indices()
        row_number = index[0]
        print(dir(self))
        print(row_number)
        

        return 1


    def __init__( self ):
        builder = Gtk.Builder()
        builder.add_from_file( "test.glade" )
        
        self.window = builder.get_object( "window1" )
        print(builder.get_objects())
        builder.get_objects()
        self.stagingarea = builder.get_object( "stagingarea" )
        self.stagingstore = builder.get_object( "stagingstore" )
        self.archivearea = builder.get_object( "archivearea" )
        self.archivestore = builder.get_object( "archivestore" )


        builder.connect_signals( self )

if __name__ == "__main__":
    win = Sample()
    win.window.show_all()
    Gtk.main()
