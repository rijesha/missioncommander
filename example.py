from gi.repository import Gtk

software_list = [("Firefox", 2002),
                 ("Eclipse", 2004),
                 ("Pitivi", 2004),
                 ("Netbeans", 1996),
                 ("Chrome", 2008),
                 ("Filezilla", ),
                 ("Bazaar", 2005),
                 ("Git", 2005),
                 ("Linux Kernel", 1991),
                 ("GCC", 1987),
                 ("Frostwire", 2004)]





builder = Gtk.Builder()
builder.add_from_file("test.glade")

window = builder.get_object("window1")
stagingarea = builder.get_object("CommandArchive")

software_liststore = Gtk.ListStore(str, int)
for software_ref in software_list:
    software_liststore.append(list(software_ref))

stagingarea.Model = software_liststore


window.show_all()

Gtk.main()

