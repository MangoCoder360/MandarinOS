def init():
    try:
        global setup
        accnt_status = open('accnt_status.pkl','r')
        setup = pickle.load(accnt_status)
        accnt_status.close()
    except:
        easygui.msgbox('Please activate the software using the provided activation tool','Mandarin Bootloader Managment Console')

def setupWizard():
    global setup1
    easygui.msgbox('Welcome to Mandarin OS! Lets get started!', 'System Boot Wizard')
    easygui.msgbox('To create your Computer Account please choose a username and password','Account Creation Wizard')
    accnt_usrname1 = easygui.enterbox('Username','Account Creation Wizard')
    accnt_psswrd1 = easygui.enterbox('Password','Account Creation Wizard')
    accnt_psswrd = open('accnt_psswrd.pkl','w')
    accnt_usrname = open('accnt_usrname.pkl','w')
    pickle.dump(accnt_usrname1, accnt_usrname)
    pickle.dump(accnt_psswrd1, accnt_psswrd)
    set_up = True
    accnt_status = open('accnt_status.pkl','w')
    pickle.dump(set_up, accnt_status)
    accnt_status.close()

def SunriverCam():
    webbrowser.open('https://www.tripcheck.com/roadcams/cams/LavaButte_pid631.jpg')
    desktop()

def desktop():
    appOptions = ['SunriverCam', 'Shutdown']
    appToOpen = easygui.buttonbox("Choose an app to open!", choices = appOptions)
    if appToOpen == "SunriverCam":
        SunriverCam()
    
def loginWizard():
    usr_enter = easygui.enterbox('Please enter your username','Login Wizard')
    pss_enter = easygui.enterbox('Please enter your password','Login Wizard')
    real_usr1 = open('accnt_usrname.pkl','r')
    real_pss1 = open('accnt_psswrd.pkl','r')
    real_usr = pickle.load(real_usr1)
    real_pss = pickle.load(real_pss1)
    if usr_enter == real_usr and pss_enter == real_pss:
        desktop()
    else:
        easygui.msgbox("The username or password you entered is incorrect!")

import easygui
import pickle
import time
import webbrowser
import updateCheck
import elevate
elevate.elevate()
time.sleep(2)
print 'MANDARIN OS >>> Welcome to Mandarin OS, your system is starting! Get ready!'
time.sleep(1)
currentVer = "1.0.8"
setup = None
init()
if setup == False:
    setupWizard()
elif setup == True:
    loginWizard()
