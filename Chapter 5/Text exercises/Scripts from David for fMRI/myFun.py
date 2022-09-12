'''
This is a collection of small functions that are of general use
over multiple experiments

v 01.00.00 17.08.2016:  - function added: get a string inputText 
                        - function added: create a .csv datafile for logging responses
                        - function added: show a text on screen (center)
                        - function added: show a text on screen (custom position)
                        - function added: show a countdown on screen (3...2...1...)
                        - function added: create a fixation cross stimulus
v 01.01.00 14.12.2016:  - function added: wait for mouse click 


by David Wisniewski (david.wisniewski@ugent.be)
'''
  
from psychopy import core, visual, event, clock
import csv, os, time
from ctypes import windll

# Get a string input
def getString(window, question="Type: text followed by return"):
    string = ""
    while True:
        message = visual.TextStim(window, text=question+string, color = 'white')
        message.draw()
        window.flip()
        c = event.waitKeys()
        if c[0] == 'return':
            return string
        else:
            string = string + c[0]

# Create a log file (.csv format) with a user-specififed file name
# format: Sub[subjectnumber]_[custom string]_[current date and time].csv
def openDataFile(ppn=0,type='default_setting'):
    # pick a directory
	directory = "F:/Data/Projects/2017_01_IntRew_Exp1/3-ExperimentBehPilot1/2-RawData"
    if not os.path.isdir(directory):
        os.mkdir(directory)
    try:
		#automatically append the date and time to the filename to avoid filename conflicts
        filename="{}/Sub{}_{}_{}.csv".format(directory, '{:02g}'.format(ppn), type, time.strftime('D%Y-%m-%d_T%H:%M:%S')) # ISO compliant
        datafile = open(filename, 'wb')
    except Exception as e:
        filename="{}/Sub{}_{}_{}.csv".format(directory, '{:02g}'.format(ppn), type, time.strftime('D%Y-%m-%d_T%H-%M-%S')) #for MS Windows
        datafile = open(filename, 'wb')
    return datafile          

# show text in the center of the screen
def showText(window, inputText="Text"):
    message = visual.TextStim(window, alignHoriz="center", alignVert="center",text=inputText, color = 'white', font='Lucida Sans', wrapWidth=20, height=1)
    message.draw()
    window.flip()

# show text on a custom position on the screen
def showTextPos(window, inputText="Text", x=0, y=0):
    message = visual.TextStim(window, alignHoriz="center", alignVert="center",text=inputText, color = 'white', font='Lucida Sans', wrapWidth=20, height=1, pos=(x,y))
    message.draw()
    window.flip()

# show a countdown on screen
def showCountdown (window):
    times = [3, 2, 1]
    for t in times:
        timer = visual.TextStim(window, alignHoriz="center", alignVert="center",text=str(t) , color = 'white', height=1.5, font='Lucida Sans')
        timer.draw()
        window.flip()
        core.wait(1)
    
# generate fixation cross
def genFix (window):
    fixsize = 0.6   #simple handle on fixation cross size
    fixVertices = [[0.0,0.0], [0.0,-fixsize], [0.0,fixsize], [0.0,0.0], [fixsize,0.0], [-fixsize,0.0], [0.0,0.0]]
    fixation = visual.ShapeStim(window, vertices=fixVertices, pos=[0,0], lineColor= 'white', lineWidth=3.0, closeShape=False, opacity= 1.0,units='cm')
    return fixation

# wait until the mouse button 0 is pressed
def waitClick ():
    myMouse = event.Mouse()
    oldMouseIsDown = False
    while True:
        mouseIsDown = myMouse.getPressed()[0]
        myMouse.clickReset()
        if mouseIsDown and not oldMouseIsDown:
            print myMouse.getPos()
            print('Mouse button pressed')
            break
        oldMouseIsDown = mouseIsDown

