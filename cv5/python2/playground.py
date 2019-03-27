# 
#  Playground module for SPJA
#  Stanislav Bohm
#
#  Public API:
#  function: "run", see example1 and example2 for details
#

import gtk
import gobject as glib

class PlaygroundView(gtk.DrawingArea):
	
	def __init__(self):
		gtk.DrawingArea.__init__(self)
		
		self.circles = []

		cmap = self.get_colormap()
		self.color_bg = cmap.alloc_color('#000000')
		self.color_c1 = cmap.alloc_color('#00FF00')
		self.color_c2 = cmap.alloc_color('#FFFFFF')

		self.connect("expose_event", self._exposeEvent)
		self.set_events(gtk.gdk.EXPOSURE_MASK)

	def set_circles(self, circles):
		self.circles = circles

	def get_sizes(self):
		alloc = self.get_allocation()
		return (alloc.width, alloc.height)

	def _exposeEvent(self, widget, event):
		alloc = self.get_allocation()
		gc = self.window.new_gc()
		self.window.begin_paint_rect(alloc)
		try:
			gc.set_foreground(self.color_bg)
			self.window.draw_rectangle(gc, True, 0,0, alloc.width, alloc.height)
			self._drawCircles(gc)
		finally:
			self.window.end_paint()

	def _drawCircles(self, gc):
		gc.set_foreground(self.color_c1)
		for x, y, r in self.circles:		
			self.window.draw_arc(gc, True, int(x - r), int(y - r), int(r * 2), int(r * 2), 0, 365 * 64)

		gc.set_foreground(self.color_c2)
		for x, y, r in self.circles:		
			self.window.draw_arc(gc, False, int(x - r), int(y - r), int(r * 2), int(r * 2), 0, 365 * 64)


class PlaygroundWindow(gtk.Window):
	def __init__(self, viewsize):
		gtk.Window.__init__(self)
		self.set_title("Playground window")
		self.connect("destroy", gtk.main_quit)
		self.pv = PlaygroundView()
		self.pv.set_size_request(viewsize[0], viewsize[1])
		self.add(self.pv)
		self.pv.show()

	def set_circles(self, circles):
		self.pv.set_circles(circles)

	def get_playground_view_sizes(self):
		return self.pv.get_sizes()

	def redraw(self):
		return self.pv.queue_draw()

def refresh(window, world):		
	sx, sy = window.get_playground_view_sizes()
	window.set_circles(world.tick(sx, sy))
	window.redraw()
	return True

def run(viewsize, world):
	window = PlaygroundWindow(viewsize)
	window.show()
	timer_id = glib.timeout_add(30, refresh, window, world)
	try:
		gtk.main()
	finally:
		glib.source_remove(timer_id)
