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
import sentry_sdk
sentry_sdk.init("https://7cba374024ca45eb9b4fdef818721b52@o464050.ingest.sentry.io/5516881", traces_sample_rate=1.0)
sysVer = "1.2.0\n" # Newline character required due to github file structure
desktop()
