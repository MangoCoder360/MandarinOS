import easygui
import subprocess
import sentry_sdk
sentry_sdk.init("https://7cba374024ca45eb9b4fdef818721b52@o464050.ingest.sentry.io/5516881", traces_sample_rate=1.0)
chs = ["Offline Mode (local user data storage)", "Online Mode (fetch user data from MongoDB database)"]
answer = easygui.buttonbox("Welcome to MandarinOS! Please choose which version of MandarinOS you would like to run today.", choices = chs)
if answer == "Offline Mode (local user data storage)":
    subprocess.call("OfflineMandarin.py", shell=True)
if answer == "Online Mode (fetch user data from MongoDB database)":
    subprocess.call("OnlineMandarinBase.py", shell=True)
