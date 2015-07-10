#!/usr/bin/env python

import cairo
from gi.repository import Gtk, Gdk

class MyWin (Gtk.Window):
	def __init__(self):
		super(MyWin, self).__init__()
		self.set_position(Gtk.WindowPosition.CENTER)
		self.set_border_width(30)
		self.screen = self.get_screen()
		self.visual = self.screen.get_rgba_visual()
		if self.visual != None and self.screen.is_composited():
		    print "yay"
		    self.set_visual(self.visual)

		box = Gtk.Box()
		btn1 = Gtk.Button(label="foo")
		box.add(btn1)
		self.add(box)
		self.connect("delete-event", Gtk.main_quit)
		self.set_app_paintable(True)
		self.connect("draw", self.area_draw)
		self.show_all()
		self.get_window().set_decorations(Gdk.WMDecoration.BORDER)
	def area_draw(self, widget, cr):
		cr.set_source_rgba(.2, .2, .2, 0.9)
		cr.set_operator(cairo.OPERATOR_SOURCE)
		cr.paint()
		cr.set_operator(cairo.OPERATOR_OVER)

MyWin()
Gtk.main()
