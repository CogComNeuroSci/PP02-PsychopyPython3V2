# Draw a square in a Window that is exactly four visual degrees (irrespective of screen physical properties).

from psychopy import visual
import time 

win = visual.Window(fullscr = True, monitor = "testMonitor", units = "deg")
rect = visual.Rect(win, width = 4, height = 4)

rect.draw()
win.flip()
time.sleep(2)
win.close()