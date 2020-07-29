def init():
    global setup
    accnt_status = open('accnt_status.pkl','r')
    setup = pickle.load(accnt_status)
    accnt_status.close()

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

def desktop():
    easygui.msgbox('Hello there, I am the computer I am here to tell you that this is as far as the program will go for a while,','Desktop')
    easygui.msgbox('My programmers are stumped at how to create a functional desktop with apps and everything, so please note there will be no desktop for quite a while.','Desktop')
    
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
print 'Checking Files'
time.sleep(0.2)
print 'Verifing Checksum'
time.sleep(1)
print 'Initializing BIOS'
time.sleep(0.5)
print 'Starting Pre-boot sequence'
time.sleep(0.5)
print 'Initializing Boot Sequence'
time.sleep(1.2)
print 'Checking HD-RW-HS CD-ROM'
time.sleep(0.2)
print 'Checking SYSINT-MNDRN_SATA-HD'
time.sleep(0.2)
print 'Reading data in SYSINT-MNDRN_SATA-HD'
time.sleep(1.8)
print 'Booting MANDARIN-OS-MEDIA in SYSINT-MNDRN_SATA-HD'
print ''
time.sleep(2.5)
print 'MANDARIN OS >>> Welcome to Mandarin OS, your system is starting!'
time.sleep(3)
setup = 0
init()
if setup == False:
    setupWizard()
else:
    loginWizard()
