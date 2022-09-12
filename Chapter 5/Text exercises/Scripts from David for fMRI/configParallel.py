
'''
Send a trigger through the parallel port

This script works on the experimental PC of the GifMI @UZ Gent.
You need a parallel port driver installed for this to work, 
which is installed on that PC already.

v 01.00.00	13.07.2017:	- sends a trigger through the parallel port

by David Wisniewski (david.wisniewski@ugent.be)

'''

# send parallel port trigger
# just pick the trigger to send (0-255) and the duration of the pulse 
def sendpport(port=0XBC00,trigger=255, duration=0.05):
    windll.inpout32.Out32(port,trigger)
    core.wait(duration)
    windll.inpout32.Out32(port,0)