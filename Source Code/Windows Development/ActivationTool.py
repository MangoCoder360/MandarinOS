import easygui
import pickle
import elevate
import sentry_sdk
sentry_sdk.init("https://7cba374024ca45eb9b4fdef818721b52@o464050.ingest.sentry.io/5516881", traces_sample_rate=1.0)
elevate.elevate()
def activate():
    setup = False
    accnt_status = open('accnt_status.pkl','w')
    pickle.dump(setup,accnt_status)
    accnt_status.close()
    easygui.msgbox('Your program has been activated! Thank you for chosing Mandarin Technologies!','ActivationTool')

serNumEnter = easygui.enterbox('Please enter your serial number to activate the program','ActivationTool')
realSerNum = 'MANDARIN97831'
realSerNum2 = '367-882-925'
realSerNum3 = 'MANDARINOS775'
if serNumEnter == realSerNum or serNumEnter == realSerNum2 or serNumEnter == realSerNum3:
    easygui.msgbox('Verified, your program is activating...','ActivationTool')
    activate()
else:
    easygui.msgbox('ERROR: Invalid Serial Number Entered','ActivationTool')
