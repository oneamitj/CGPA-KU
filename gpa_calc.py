#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import os

class NumberEntry(gtk.Entry):
    def __init__(self):
        gtk.Entry.__init__(self)
        self.connect('changed', self.on_changed)

    def on_changed(self, *args):
        text = self.get_text().strip()
        self.set_text(''.join([i for i in text if i in '0123456789.']))


class gpa:
    global label
    # This is a callback function. The data arguments are ignored
    # in this example. More on callbacks below.

    def delete_event(self, widget, event, data=None):
        print "delete event occurred"
        return False

    def destroy(self, widget, data=None):
        print "destroy signal occurred"
        gtk.main_quit()
        global check
        check = 1

    def gpa_calc(self,widget,*data):
    	sem1 = float(self.entry_sem1.get_text().strip())
    	sem2 = float(self.entry_sem2.get_text().strip())
    	sem3 = float(self.entry_sem3.get_text().strip())
    	sem4 = float(self.entry_sem4.get_text().strip())
    	sem5 = float(self.entry_sem5.get_text().strip())
    	sem6 = float(self.entry_sem6.get_text().strip())
    	sem7 = float(self.entry_sem7.get_text().strip())
    	sem8 = float(self.entry_sem8.get_text().strip())
    	# #gpa = (int(a)*20+int(b)*20+int(c)*18+int(d)*18+int(e)*+int(f)*19+int(g)*18+int(h)*12)/143
    	gpa = (sem1*20 + sem2*20 + sem3*18 + sem4*18 + sem5*18 + sem6*19 + sem7*18 + sem8*12)/143
    	print gpa
    	self.label_cgpa.set_label(str(gpa))

    def __init__(self):
        global label
        # create a new window
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("delete_event", self.delete_event)
        self.window.set_keep_above(True)
        self.window.set_title("GPA")
        self.window.set_default_size(20,50)
        self.window.connect("destroy", self.destroy)
        self.window.set_border_width(10)

        self.button = gtk.Button("Calculate")


        self.entry_sem1 = NumberEntry()
        self.entry_sem2 = NumberEntry()
        self.entry_sem3 = NumberEntry()
        self.entry_sem4 = NumberEntry()
        self.entry_sem5 = NumberEntry()
        self.entry_sem6 = NumberEntry()
        self.entry_sem7 = NumberEntry()
        self.entry_sem8 = NumberEntry()

        self.label_sem1 = gtk.Label("1st Sem")
        self.label_sem2 = gtk.Label("2nd Sem")
        self.label_sem3 = gtk.Label("3rd Sem")
        self.label_sem4 = gtk.Label("4th Sem")
        self.label_sem5 = gtk.Label("5th Sem")
        self.label_sem6 = gtk.Label("6th Sem")
        self.label_sem7 = gtk.Label("7th Sem")
        self.label_sem8 = gtk.Label("8th Sem")
        self.label_gpa = gtk.Label("GPA = ")
        self.label_cgpa = gtk.Label(" ")

        self.vbox = gtk.VBox(gtk.FALSE, 10)
        self.hbox1 = gtk.HBox(gtk.FALSE, 5)
        self.hbox2 = gtk.HBox(gtk.FALSE, 5)
        self.hbox3 = gtk.HBox(gtk.FALSE, 5)
        self.hbox4 = gtk.HBox(gtk.FALSE, 5)
        self.gpa_box = gtk.HBox(gtk.FALSE, 5)


        self.hbox1.pack_start(self.label_sem1, gtk.FALSE, gtk.FALSE, 0)
        self.label_sem1.show()
        self.hbox1.pack_start(self.entry_sem1, gtk.FALSE, gtk.FALSE, 0)
        self.entry_sem1.show()

        self.hbox1.pack_start(self.label_sem2, gtk.FALSE, gtk.FALSE, 0)
        self.label_sem2.show()
        self.hbox1.pack_start(self.entry_sem2, gtk.FALSE, gtk.FALSE, 0)
        self.entry_sem2.show()


        self.hbox2.pack_start(self.label_sem3, gtk.FALSE, gtk.FALSE, 0)
        self.label_sem3.show()
        self.hbox2.pack_start(self.entry_sem3, gtk.FALSE, gtk.FALSE, 0)
        self.entry_sem3.show()

        self.hbox2.pack_start(self.label_sem4, gtk.FALSE, gtk.FALSE, 0)
        self.label_sem4.show()
        self.hbox2.pack_start(self.entry_sem4, gtk.FALSE, gtk.FALSE, 0)
        self.entry_sem4.show()


        self.hbox3.pack_start(self.label_sem5, gtk.FALSE, gtk.FALSE, 0)
        self.label_sem5.show()
        self.hbox3.pack_start(self.entry_sem5, gtk.FALSE, gtk.FALSE, 0)
        self.entry_sem5.show()

        self.hbox3.pack_start(self.label_sem6, gtk.FALSE, gtk.FALSE, 0)
        self.label_sem6.show()
        self.hbox3.pack_start(self.entry_sem6, gtk.FALSE, gtk.FALSE, 0)
        self.entry_sem6.show()


        self.hbox4.pack_start(self.label_sem7, gtk.FALSE, gtk.FALSE, 0)
        self.label_sem7.show()
        self.hbox4.pack_start(self.entry_sem7, gtk.FALSE, gtk.FALSE, 0)
        self.entry_sem7.show()

        self.hbox4.pack_start(self.label_sem8, gtk.FALSE, gtk.FALSE, 0)
        self.label_sem8.show()
        self.hbox4.pack_start(self.entry_sem8, gtk.FALSE, gtk.FALSE, 0)
        self.entry_sem8.show()

        self.gpa_box.pack_start(self.label_gpa, gtk.FALSE, gtk.FALSE, 0)
        self.label_gpa.show()
        self.gpa_box.pack_start(self.label_cgpa, gtk.FALSE, gtk.FALSE, 0)
        self.label_cgpa.show()

        self.vbox.pack_start(self.hbox1, gtk.FALSE, gtk.FALSE, 0)
        self.hbox1.show()
        self.vbox.pack_start(self.hbox2, gtk.FALSE, gtk.FALSE, 0)
        self.hbox2.show()
        self.vbox.pack_start(self.hbox3, gtk.FALSE, gtk.FALSE, 0)
        self.hbox3.show()
        self.vbox.pack_start(self.hbox4, gtk.FALSE, gtk.FALSE, 0)
        self.hbox4.show()
        self.vbox.pack_start(self.gpa_box, gtk.FALSE, gtk.FALSE, 0)
        self.gpa_box.show()        

        #self.gpa_calc(self.entry_sem1.get_text().strip(), self.entry_sem2.get_text().strip(), self.entry_sem3.get_text().strip(), self.entry_sem4.get_text().strip(), self.entry_sem5.get_text().strip(), self.entry_sem6.get_text().strip(), self.entry_sem7.get_text().strip(), self.entry_sem8.get_text().strip())
        self.button.connect("clicked", self.gpa_calc)#, self.entry_sem1.get_text().strip(), self.entry_sem2.get_text().strip(), self.entry_sem3.get_text().strip(), self.entry_sem4.get_text().strip(), self.entry_sem5.get_text().strip(), self.entry_sem6.get_text().strip(), self.entry_sem7.get_text().strip(), self.entry_sem8.get_text().strip())

        self.vbox.pack_start(self.button, gtk.FALSE, gtk.FALSE, 0)
        self.button.show()

        self.vbox.show()

        self.window.add(self.vbox)
        self.window.show()

    def main(self):
        gtk.main()

# If the program is run directly or passed as an argument to the python
# interpreter then create a HelloWorld instance and show it
if __name__ == "__main__":
    gpa_main = gpa()
    gpa_main.main()