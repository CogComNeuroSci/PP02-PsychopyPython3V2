
'''
Configure serial devices 

Currently supported devices:
	- MR scanner (@GifMI, UZ Gent)
	- Digitimer DS7A shocking device 
		(connected through an Arduino control box made by pascal.mestdagh@ugent.be
		requires Arduino driver to work)

v 01.00.00	17.07.2017	- supported devices: GifMI MR scanner, Digitimer DS7A

by David Wisniewski (david.wisniewski@ugent.be)

'''
import serial
from psychopy import core, event

##########
## FMRI ##
##########

# initialize the MR scanner port
def init_scannerSync():
    global scannerSync
	# on the experimental PC, the scanner port is COM1
    scannerSync = serial.Serial('COM1',9600,timeout=1)
	# check whether it is open 
    if scannerSync.isOpen():        
        print 'Open: ' + scannerSync.portstr + ', baudrate: ' + str(scannerSync.baudrate)

# wait for the first MR trigger pulse to start the experiment
def waitForExptStartTrigger():
	# remove any keys waiting in the queue
	event.clearEvents(eventType='keyboard') 
	while True:
		# the MRI 'start' code is '5', sent through the serial port
        if (scannerSync.read() == '5'): 
            print('MRI trigger received!')
			# begin the experiment
            break 
		# if you press Escape, you manually exit the while loop
        key = event.getKeys() 
        if len(key) > 0:
            if key == ['escape']: core.quit() 
            break 

# close the MR scanner port     
def close_scannerSync():
    scannerSync.close()
    print 'Closed serial port to MRI'

###############
## DIGITIMER ##
###############

# initialize serial port to shocking device
def init_serial_shock():
    # initialize serial port used by Arduino (linked to DS7A shock device)
	# make sure the correct COM port is specified here
    serShock = serial.Serial('COM14',9600)
    # check whether it is open 
    if serShock.isOpen():                               
        print 'Open: ' + serShock.portstr + ', baudrate: ' + str(serShock.baudrate)
    else:
        print 'No serial port was opened'    
    core.wait(2)
    return serShock

# configure the shocks (repetitions and interval)
# to set the numer of pulse repetitions, send this string: r000, where 000 is the number of repetitions
# to set the interval between the pulses, send this strong: i000, where 000 is the duration between pulses in ms
def config_serial_shock(serShock,r=1,i=1):
    rToSend='{:03g}'.format(r)
    print 'Set Repetions to ' + rToSend
    iToSend='{:03g}'.format(i)
    print 'Set Interval to ' + iToSend
    serShock.write('r'+rToSend)
    core.wait(2)
    serShock.write('i'+iToSend)
    print 'Configuration of shock device changed'

# apply shock once
def apply_serial_shock(serShock):
    # the Arduino control box applies the configured shock once after receiving 'a000'
	serShock.write('a000')

# switch display on or off
# this switches the display of the Arduino box on and off (does not affect Digitimer directly)
# if you apply many shocks in a short time, it is useful to switch the display off, as the Arduino
# can only handle 1 command every 100ms with the display switched on.
def swtich_display(serShock):
    serShock.write('d000')

# close serial port to shocking device
def close_serial_shock(serShock):
    serShock.close()
    print 'Closed serial port to shock device'

# Test code for debugging
'''
# You can use code like this to debug your serial port scripts.
s = init_serial_shock()
config_serial_shock(s,12,18)
core.wait(1)
apply_serial_shock(s)
close_serial_shock(s)
'''
