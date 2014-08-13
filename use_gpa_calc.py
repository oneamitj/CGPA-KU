#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import os
import array
import itertools





class NumberEntry(gtk.Entry):
    def __init__(self):
        gtk.Entry.__init__(self)
        self.connect('changed', self.on_changed)


    def on_changed(self, *args):
        text = self.get_text().strip()
        self.set_text(''.join([i for i in text if i in '0123456789.']))





class gpa:
    def delete_event(self, widget, event, data=None):
        print "delete event occurred"
        return False



    def destroy(self, widget, data=None):
        print "destroy signal occurred"
        gtk.main_quit()


    def cgpa_calc(self,widget,*data):
    	crd = 0
    	sem = array.array('f', [0.0]) * 9
    	if (self.entry_sem1.flags() & gtk.VISIBLE != 0):
            sem[1] = float(self.entry_sem1.get_text().strip())
            crd = crd + self.cr[1]
        else:
            sem[1] = 0
        if (self.entry_sem2.flags() & gtk.VISIBLE != 0):
            sem[2] = float(self.entry_sem2.get_text().strip())
            crd = crd + self.cr[2]
        else:
            sem[2] = 0
        if (self.entry_sem3.flags() & gtk.VISIBLE != 0):
            sem[3] = float(self.entry_sem3.get_text().strip())
            crd = crd + self.cr[3]
        else:
            sem[3] = 0
        if (self.entry_sem4.flags() & gtk.VISIBLE != 0):
            sem[4] = float(self.entry_sem4.get_text().strip())
            crd = crd + self.cr[4]
        else:
            sem[4] = 0
        if (self.entry_sem5.flags() & gtk.VISIBLE != 0):
            sem[5] = float(self.entry_sem5.get_text().strip())
            crd = crd + self.cr[5]
        else:
            sem[5] = 0
        if (self.entry_sem6.flags() & gtk.VISIBLE != 0):
            sem[6] = float(self.entry_sem6.get_text().strip())
            crd = crd + self.cr[6]
        else:
            sem[6] = 0
        if (self.entry_sem7.flags() & gtk.VISIBLE != 0):
            sem[7] = float(self.entry_sem7.get_text().strip())
            crd = crd + self.cr[7]
        else:
            sem[7] = 0
        if (self.entry_sem8.flags() & gtk.VISIBLE != 0):
            sem[8] = float(self.entry_sem8.get_text().strip())
            crd = crd + self.cr[8]
        else:
            sem[8] = 0

        gpa = (sem[1]*self.cr[1] + sem[2]*self.cr[2] + sem[3]*self.cr[3] + sem[4]*self.cr[4] + sem[5]*self.cr[5] + sem[6]*self.cr[6] + sem[7]*self.cr[7] + sem[8]*self.cr[8])/crd
        self.label_cgpa.set_label(str(gpa))



    def department(self, widget, value, a,b,c,d,e,f,g,h):     
        active = widget.get_active()
        if value == "CE" and active == True:
            print "1"
            self.cr[1] = 20
            self.cr[2] = 20
            self.cr[3] = 18
            self.cr[4] = 18
            self.cr[5] = 18
            self.cr[6] = 19
            self.cr[7] = 18
            self.cr[8] = 12            
        elif value == "EE" and active == True:
            print "2"
            self.cr[1] = 20
            self.cr[2] = 20
            self.cr[3] = 19
            self.cr[4] = 19
            self.cr[5] = 18
            self.cr[6] = 18
            self.cr[7] = 18
            self.cr[8] = 18



    def gpa_calc(self, widget):
        grade = 1.0
        cr_gp = 0
        gp = 0
        sem = array.array('f', [0.0]) * 9

        if (self.entry_sem1.flags() & gtk.VISIBLE != 0):
            sem[1] = float(self.entry_sem1.get_text().strip())
        else:
            sem[1] = grade
        if (self.entry_sem2.flags() & gtk.VISIBLE != 0):
            sem[2] = float(self.entry_sem2.get_text().strip())
        else:
            sem[2] = grade
        if (self.entry_sem3.flags() & gtk.VISIBLE != 0):
            sem[3] = float(self.entry_sem3.get_text().strip())
        else:
            sem[3] = grade
        if (self.entry_sem4.flags() & gtk.VISIBLE != 0):
            sem[4] = float(self.entry_sem4.get_text().strip())
        else:
            sem[4] = grade
        if (self.entry_sem5.flags() & gtk.VISIBLE != 0):
            sem[5] = float(self.entry_sem5.get_text().strip())
        else:
            sem[5] = grade
        if (self.entry_sem6.flags() & gtk.VISIBLE != 0):
            sem[6] = float(self.entry_sem6.get_text().strip())
        else:
            sem[6] = grade
        if (self.entry_sem7.flags() & gtk.VISIBLE != 0):
            sem[7] = float(self.entry_sem7.get_text().strip())
        else:
            sem[7] = grade
        if (self.entry_sem8.flags() & gtk.VISIBLE != 0):
            sem[8] = float(self.entry_sem8.get_text().strip())
        else:
            sem[8] = grade
        cgpa = float(self.entry_cgpa.get_text().strip())
        crd = self.cr[1] + self.cr[2] + self.cr[3] + self.cr[4] + self.cr[5] + self.cr[6] + self.cr[7] + self.cr[8]

        colxn_entry = [self.entry_sem1, self.entry_sem2, self.entry_sem3, self.entry_sem4, self.entry_sem5, self.entry_sem6, self.entry_sem7, self.entry_sem8]
        colxn_label = [self.label_sem1, self.label_sem2, self.label_sem3, self.label_sem4, self.label_sem5, self.label_sem6, self.label_sem7, self.label_sem8]
        
        j = 0
        for i in colxn_entry:
            j = j + 1
            if (i.flags() & gtk.VISIBLE == 0):
                cr_gp = cr_gp + self.cr[j]
            elif (i.flags() & gtk.VISIBLE != 0):
                gp = gp + (sem[j] * self.cr[j])
        
        grade = ((cgpa * crd)-gp)/cr_gp

        for i in colxn_label:
            i.set_text(str(grade))
            


    def state(self, widget, widget1, widget2):
        value = widget.get_active()
        if value == False:
            widget1.show()
            widget2.hide()
        else:
            widget2.show()        
            widget1.hide()

    def calculate(self, widget, widget1, widget2, value):
        active = widget.get_active()
        if value == 1 and active == True:
            #print active, value
            widget1.show()
            widget2.hide()
            self.check_cgpa.set_active(False)
            self.label_cgpa.show()
            self.entry_cgpa.hide()
        elif value == 2 and active == True:
            #print active, value
            widget2.show()
            widget1.hide()
            self.check_cgpa.set_active(True)
            self.label_cgpa.hide()
            self.entry_cgpa.show()



    def __init__(self):
        self.cr = array.array('i', [0]) * 9        
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("delete_event", self.delete_event)
        self.window.set_keep_above(True)
        self.window.set_title("GPA:: C.E.")
        self.window.set_default_size(20,50)
        self.window.connect("destroy", self.destroy)
        self.window.set_border_width(10)

        self.button1 = gtk.Button("Calculate CGPA")
        self.button2 = gtk.Button("Calculate GPA")

        self.radio1 = gtk.RadioButton(None,"CGPA")
        self.radio2 = gtk.RadioButton(self.radio1,"GPA (uncheck those sem whose GPA is to predict)")
        self.radio1.set_active(True)
        
        self.dept_box = gtk.HBox(gtk.FALSE, 5)

        self.dept = gtk.RadioButton(None,"DoEE")
        self.dept.connect("toggled", self.department, "EE", self.cr[1], self.cr[2], self.cr[3], self.cr[4], self.cr[5], self.cr[6], self.cr[7], self.cr[8])
        self.dept_box.pack_start(self.dept, gtk.FALSE, gtk.FALSE, 0)
        self.dept.show()

        self.dept = gtk.RadioButton(self.dept,"DoCE")
        self.dept.connect("toggled", self.department, "CE", self.cr[1], self.cr[2], self.cr[3], self.cr[4], self.cr[5], self.cr[6], self.cr[7], self.cr[8])
        self.dept_box.pack_start(self.dept, gtk.FALSE, gtk.FALSE, 0)
        self.dept.show()
        self.dept.set_active(True)


        self.entry_sem1 = NumberEntry()
        self.entry_sem2 = NumberEntry()
        self.entry_sem3 = NumberEntry()
        self.entry_sem4 = NumberEntry()
        self.entry_sem5 = NumberEntry()
        self.entry_sem6 = NumberEntry()
        self.entry_sem7 = NumberEntry()
        self.entry_sem8 = NumberEntry()

        self.label_sem1 = gtk.Label("          ")
        self.label_sem2 = gtk.Label("          ")
        self.label_sem3 = gtk.Label("          ")
        self.label_sem4 = gtk.Label("          ")
        self.label_sem5 = gtk.Label("          ")
        self.label_sem6 = gtk.Label("          ")
        self.label_sem7 = gtk.Label("          ")
        self.label_sem8 = gtk.Label("          ")

        self.check_sem1 = gtk.CheckButton("1st Sem")
        self.check_sem2 = gtk.CheckButton("2nd Sem")
        self.check_sem3 = gtk.CheckButton("3rd Sem")
        self.check_sem4 = gtk.CheckButton("4th Sem")
        self.check_sem5 = gtk.CheckButton("5th Sem")
        self.check_sem6 = gtk.CheckButton("6th Sem")
        self.check_sem7 = gtk.CheckButton("7th Sem")
        self.check_sem8 = gtk.CheckButton("8th Sem")
        
        self.check_cgpa = gtk.CheckButton("CGPA = ")
        self.label_cgpa = gtk.Label("          ")
        self.entry_cgpa = NumberEntry()

        self.vbox = gtk.VBox(gtk.FALSE, 10)
        self.radio_box = gtk.HBox(gtk.FALSE, 5)
        self.hbox1 = gtk.HBox(gtk.FALSE, 5)
        self.hbox2 = gtk.HBox(gtk.FALSE, 5)
        self.hbox3 = gtk.HBox(gtk.FALSE, 5)
        self.hbox4 = gtk.HBox(gtk.FALSE, 5)
        self.gpa_box = gtk.HBox(gtk.FALSE, 5)
        
        self.radio_box.pack_start(self.radio1, gtk.FALSE, gtk.FALSE, 0)
        self.radio1.show()
        self.radio_box.pack_start(self.radio2, gtk.FALSE, gtk.FALSE, 0)
        self.radio2.show()

        self.check_sem1.set_active(True)
        self.hbox1.pack_start(self.check_sem1, gtk.FALSE, gtk.FALSE, 0)
        self.check_sem1.show()
        self.hbox1.pack_start(self.label_sem1, gtk.FALSE, gtk.FALSE, 0)
        self.hbox1.pack_start(self.entry_sem1, gtk.FALSE, gtk.FALSE, 0)
        self.entry_sem1.show()
        self.check_sem1.connect("toggled", self.state, self.label_sem1, self.entry_sem1)

        self.check_sem2.set_active(True)
        self.hbox1.pack_start(self.check_sem2, gtk.FALSE, gtk.FALSE, 0)
        self.check_sem2.show()
        self.hbox1.pack_start(self.label_sem2, gtk.FALSE, gtk.FALSE, 0)
        self.hbox1.pack_start(self.entry_sem2, gtk.FALSE, gtk.FALSE, 0)
        self.entry_sem2.show()
        self.check_sem2.connect("toggled", self.state, self.label_sem2, self.entry_sem2)

        self.check_sem3.set_active(True)
        self.hbox2.pack_start(self.check_sem3, gtk.FALSE, gtk.FALSE, 0)
        self.check_sem3.show()
        self.hbox2.pack_start(self.label_sem3, gtk.FALSE, gtk.FALSE, 0)
        self.hbox2.pack_start(self.entry_sem3, gtk.FALSE, gtk.FALSE, 0)
        self.entry_sem3.show()
        self.check_sem3.connect("toggled", self.state, self.label_sem3, self.entry_sem3)

        self.check_sem4.set_active(True)
        self.hbox2.pack_start(self.check_sem4, gtk.FALSE, gtk.FALSE, 0)
        self.check_sem4.show()
        self.hbox2.pack_start(self.label_sem4, gtk.FALSE, gtk.FALSE, 0)
        self.hbox2.pack_start(self.entry_sem4, gtk.FALSE, gtk.FALSE, 0)
        self.entry_sem4.show()
        self.check_sem4.connect("toggled", self.state, self.label_sem4, self.entry_sem4)

        self.check_sem5.set_active(True)
        self.hbox3.pack_start(self.check_sem5, gtk.FALSE, gtk.FALSE, 0)
        self.check_sem5.show()
        self.hbox3.pack_start(self.label_sem5, gtk.FALSE, gtk.FALSE, 0)
        self.hbox3.pack_start(self.entry_sem5, gtk.FALSE, gtk.FALSE, 0)
        self.entry_sem5.show()
        self.check_sem5.connect("toggled", self.state, self.label_sem5, self.entry_sem5)

        self.check_sem6.set_active(True)
        self.hbox3.pack_start(self.check_sem6, gtk.FALSE, gtk.FALSE, 0)
        self.check_sem6.show()
        self.hbox3.pack_start(self.label_sem6, gtk.FALSE, gtk.FALSE, 0)
        self.hbox3.pack_start(self.entry_sem6, gtk.FALSE, gtk.FALSE, 0)
        self.entry_sem6.show()
        self.check_sem6.connect("toggled", self.state, self.label_sem6, self.entry_sem6)

        self.check_sem7.set_active(True)
        self.hbox4.pack_start(self.check_sem7, gtk.FALSE, gtk.FALSE, 0)
        self.check_sem7.show()
        self.hbox4.pack_start(self.label_sem7, gtk.FALSE, gtk.FALSE, 0)
        self.hbox4.pack_start(self.entry_sem7, gtk.FALSE, gtk.FALSE, 0)
        self.entry_sem7.show()
        self.check_sem7.connect("toggled", self.state, self.label_sem7, self.entry_sem7)

        self.check_sem8.set_active(True)
        self.hbox4.pack_start(self.check_sem8, gtk.FALSE, gtk.FALSE, 0)
        self.check_sem8.show()
        self.hbox4.pack_start(self.label_sem8, gtk.FALSE, gtk.FALSE, 0)
        self.hbox4.pack_start(self.entry_sem8, gtk.FALSE, gtk.FALSE, 0)
        self.entry_sem8.show()
        self.check_sem8.connect("toggled", self.state, self.label_sem8, self.entry_sem8)

        self.check_cgpa.set_active(False)
        self.gpa_box.pack_start(self.check_cgpa, gtk.FALSE, gtk.FALSE, 0)
        self.check_cgpa.show()
        self.gpa_box.pack_start(self.label_cgpa, gtk.FALSE, gtk.FALSE, 0)
        self.label_cgpa.show()
        self.gpa_box.pack_start(self.entry_cgpa, gtk.FALSE, gtk.FALSE, 0)
        self.check_cgpa.connect("toggled", self.state, self.label_cgpa, self.entry_cgpa)


        self.vbox.pack_start(self.dept_box, gtk.FALSE, gtk.FALSE, 0)
        self.dept_box.show()
        self.vbox.pack_start(self.radio_box, gtk.FALSE, gtk.FALSE, 0)
        self.radio_box.show()
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

        self.button1.connect("clicked", self.cgpa_calc)
        self.button2.connect("clicked", self.gpa_calc)
        self.radio1.connect("toggled", self.calculate, self.button1, self.button2, 1)
        self.radio2.connect("toggled", self.calculate, self.button1, self.button2, 2)
        
        self.vbox.pack_start(self.button1, gtk.FALSE, gtk.FALSE, 0)
        self.button1.show()
        self.vbox.pack_start(self.button2, gtk.FALSE, gtk.FALSE, 0)

        self.vbox.show()

        self.window.add(self.vbox)
        self.window.show()

    def main(self):
        gtk.main()






if __name__ == "__main__":
    gpa_main = gpa()
    gpa_main.main()