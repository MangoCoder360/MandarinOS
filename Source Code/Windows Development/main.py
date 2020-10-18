import easygui
import subprocess
chs = ["Offline Mode (local user data storage)", "Online Mode (fetch user data from MongoDB database)"]
answer = easygui.buttonbox("Welcome to MandarinOS! Please choose which version of MandarinOS you would like to run today.", choices = chs)
if answer == "Offline Mode (local user data storage)":
    subprocess.call("OfflineMandarin.py", shell=True)
if answer == "Online Mode (fetch user data from MongoDB database)":
    subprocess.call("OnlineMandarinBase.py", shell=True)
