from easygui import *
from time import *
#import webbrowser

"""def SunriverCam():
	webbrowser.open('https://www.tripcheck.com/roadcams/cams/LavaButte_pid631.jpg')
	desktop()"""

def desktop():
	"""appOptions = ['SunriverCam', 'Shutdown']
	appToOpen = buttonbox("Choose an app to open!", choices = appOptions)
	if appToOpen == "SunriverCam":
		SunriverCam()"""
	msgbox("No apps avalible, sorry.",'Desktop')

msgbox("Welcome to Mandarin OS, your system is starting!","System Boot Wizard")
desktop()