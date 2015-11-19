from gi.repository import Gtk
from xmlparser import xmlreader

class DialogExample(Gtk.Dialog):

    def __init__(self, parent):
        win = MissionCommander()
        win.window.show_all()

class MissionGUI:
    def gtk_main_quit( self, window ):
        Gtk.main_quit()
        self.shutdowncb()

    def ivybind(self, ivylink):
        self.ivylink = ivylink

    def send_to_staging( self, button ):
        select = self.archivearea.get_selection()
        model, iter = select.get_selected()
        self.stagingstore.append(self.archivestore[iter][:])

    def stagingarea_to_list( self, button):
        for row in self.stagingstore:
            # Print values of all columns
            list= list + (row[:])
        return 1

    def open_new_command(self, button):
        self.newcommand.run()
        self.newcommand.destroy()
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

    def append_from_staging( self, button, selection ):
        select = self.stagingarea.get_selection()
        model, iter = select.get_selected()
        return 1

    def prepend_from_staging( self, button, selection ):
        select = self.stagingarea.get_selection()
        model, iter = select.get_selected()
        self.ivylink.add_mission_command(msg)
        return 1

    def make_ident_from_staging( self, button ):
        return 1

    def update_uav_queue( self, msg):
        self.stagingarea1.freeze_child_notify()
        self.stagingarea1.set_model(None)
        self.uavQueue.clear()
        for i in msg.fieldvalues[1]:
            if i != ",":
                self.uavQueue.append(list(i) + list((msg.fieldvalues[0], "")))
        self.stagingarea1.set_model(model=self.uavQueue) 
        self.stagingarea1.thaw_child_notify()

    def update_archive(self, command_list)
        for i in command_list:
            self.archivestore.append(i.get('name') ,i.get('id'),i.get('msg'))
        return 1


    def import_from_file( self, button ):
        xmlreader.openfile("sample.xml", update_archive)
        

    def export_to_file( self, button ):
        return 1

    def write_to_archive( self, button ):
        select = self.archivearea.get_selection()
        selected_rows = select.get_selected_rows()
        path = selected_rows[1]
        row = path[0]
        index = row.get_indices()
        row_number = index[0]
        return 1


    def __init__( self, shutdowncb = None):
        builder = Gtk.Builder()
        builder.add_from_file( "gui.glade" )
        self.shutdowncb = shutdowncb
        self.window = builder.get_object( "window1" )
        self.newcommand = builder.get_object( "dialog1" )
        self.stagingarea = builder.get_object( "stagingarea" )
        self.stagingstore = builder.get_object( "stagingstore" )
        self.archivearea = builder.get_object( "archivearea" )
        self.archivestore = builder.get_object( "archivestore" )
        self.uavQueue = builder.get_object( "uavQueue" )
        self.uavQueuestaging = builder.get_object( "uavQueuestaging" )
        self.stagingarea1 = builder.get_object("stagingarea1")

        builder.connect_signals( self )


