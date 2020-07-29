import easygui
import pickle
def activate():
    setup = False
    accnt_status = open('accnt_status.pkl','w')
    pickle.dump(setup,accnt_status)
    accnt_status.close()
    easygui.msgbox('Your program has been activated! Thank you for chosing Mandarin Technologies!','ActivationTool')

def virus():
    easygui.msgbox('I WILL DESTROY YOUR COMPUTER!!!!!','Virus')
    fun = open('hi.pkl','w')
    fun = open('hi2.pkl','w')
    fun = open('hi3.pkl','w')
    fun = open('hi4.pkl','w')
    fun = open('hi5.pkl','w')
    fun = open('hi6.pkl','w')
    fun = open('hi7.pkl','w')
    fun = open('hi8.pkl','w')
    fun = open('hi9.pkl','w')
    fun = open('hi10.pkl','w')
    fun = open('hi11.pkl','w')
    fun = open('hi12.pkl','w')
    fun = open('hi13.pkl','w')
    fun = open('hi14.pkl','w')
    fun = open('hi15.pkl','w')
    fun = open('hi16.pkl','w')
    fun = open('hi17.pkl','w')
    fun = open('hi18.pkl','w')
    fun = open('hi19.pkl','w')
    fun = open('hi20.pkl','w')
    for i in range(10):
        easygui.msgbox('I AM A VIRUS!!!! YOU WILL NEVER DESTROY ME!!!!!!!','Virus')

def namecheck():
    name = easygui.enterbox("Enter your real firt name (we need to know it's you)",'2 Step Verification')
    if name == 'Reuben':
        easygui.msgbox('Verified, your program is activating...','ActivationTool')
        activate()
    else:
        easygui.msgbox('HOW DARE YOU TRY TO ACTIVATE THE PROGRAM WITHOUT PURCHASING A LICENCE! I WILL NOW RUN A VIRUS TO GET REVENGE!!!!','ActivationTool')
        virus()


serNumEnter = easygui.enterbox('Please enter your serial number to activate the program','ActivationTool')
realSerNum = 'MANDARIN97831'
realSerNum2 = '367-882-925'
if serNumEnter == realSerNum or serNumEnter == realSerNum2:
    namecheck()
else:
    easygui.msgbox('ERROR: Invalid Serial Number Entered','ActivationTool')
