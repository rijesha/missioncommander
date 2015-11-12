from gi.repository import Gtk


class MissionCommander:
    def gtk_main_quit( self, window ):
        Gtk.main_quit()

    def send_to_staging( self, button ):
        select = self.archivearea.get_selection()
        model, iter = select.get_selected()
        self.stagingstore.append(self.archivestore[iter][:])

    def stagingarea_to_list( self, button):
        for row in self.stagingstore:
            # Print values of all columns
            list= list + (row[:])
        return 1

    def delete_from_staging( self, button ):
        select = self.stagingarea.get_selection()
        model, iter = select.get_selected()
        self.stagingstore.remove(iter)
        return 1

    def delete_from_archive( self, button ):
        select = self.archivearea.get_selection()
        model, iter = select.get_selected()
        self.archivestore.remove(iter)
        return 1

    def append_from_staging( self, button ):
        return 1

    def prepend_from_staging( self, button ):
        return 1

    def make_ident_from_staging( self, button ):
        return 1


    def import_from_file( self, button ):
        command_list = [("Firefox", "2002"),
                 ("Eclipse", "2004"),
                 ("Pitivi", "2004"),
                 ("Netbeans", "1996"),
                 ("Chrome", "2008"),
                 ("Filezilla", "23" ),
                 ("Bazaar", "2005"),
                 ("Git", "2005"),
                 ("Linux Kernel", "1991"),
                 ("GCC", "1987"),
                 ("Frostwire", "2004")]

        for i in command_list:
            self.archivestore.append(list(i))
        return 1

    def export_to_file( self, button ):
        command_list = [("Firefox", "2002"),
                 ("Eclipse", "2004"),
                 ("Pitivi", "2004"),
                 ("Netbeans", "1996"),
                 ("Chrome", "2008"),
                 ("Filezilla", "23" ),
                 ("Bazaar", "2005"),
                 ("Git", "2005"),
                 ("Linux Kernel", "1991"),
                 ("GCC", "1987"),
                 ("Frostwire", "2004")]

        for i in command_list:
            self.archivestore.append(list(i))
        return 1

    def write_to_archive( self, button ):
        select = self.archivearea.get_selection()
        selected_rows = select.get_selected_rows()
        path = selected_rows[1]
        row = path[0]
        index = row.get_indices()
        row_number = index[0]

        return 1


    def __init__( self ):
        builder = Gtk.Builder()
        builder.add_from_file( "test.glade" )
        
        self.window = builder.get_object( "window1" )
        self.stagingarea = builder.get_object( "stagingarea" )
        self.stagingstore = builder.get_object( "stagingstore" )
        self.archivearea = builder.get_object( "archivearea" )
        self.archivestore = builder.get_object( "archivestore" )

        builder.connect_signals( self )

if __name__ == "__main__":
    win = MissionCommander()
    win.window.show_all()
    Gtk.main()
