def SunriverCam():
    webbrowser.open('https://www.tripcheck.com/roadcams/cams/LavaButte_pid631.jpg')
    desktop()

def desktop():
    appOptions = ['SunriverCam', "Update Checker", 'Shutdown']
    appToOpen = easygui.buttonbox("Choose an app to open!", choices = appOptions)
    if appToOpen == "SunriverCam":
        SunriverCam()
    if appToOpen == "Update Checker":
        updateCheck()
        desktop()


import easygui
import pickle
import time
import webbrowser
from updateCheck import updateCheck
sysVer = "1.2.0\n" # Newline character required due to github file structure
desktop()
