print("Please wait while we sign you into MongoDB..")
import pymongo
import easygui
import pickle
import time
import subprocess
import sentry_sdk
sentry_sdk.init("https://7cba374024ca45eb9b4fdef818721b52@o464050.ingest.sentry.io/5516881", traces_sample_rate=1.0)
client = pymongo.MongoClient("mongodb+srv://MangoCoder360:mangomongo321@cluster0.vckzv.mongodb.net/WindowsApp?retryWrites=true&w=majority")
db = client["WindowsApp"]
coll = db["Users"]
print("Connected to MongoDB WindowsApp Server!")
loginOption = easygui.buttonbox("Welcome to MandarinOS Online! We are connected to MongoDB and are ready to start!", choices = ["Login to existing account", "Create an account", "Activate an existing account"])
if loginOption == "Login to existing account":
    username = easygui.enterbox("Enter your username:")
    password = easygui.enterbox("Enter your password:")
    getData = coll.find({"username":username}, {"password": 1, "_id": 0})
    for i in getData: data = i
    realPassword = data["password"]
    if realPassword == password:
        easygui.msgbox('You have been signed in sucsesfully! Please wait while we retrive your user data...')
        activatedRaw = coll.find({"username":username}, {"activated": 1, "_id": 0})
        for i in activatedRaw: activated = i
        if activated == True:
            subprocess.call("OnlineMandarinDesktop.py", shell=True)
        else:
            easygui.msgbox('Your account has not been activated. Please activate your account using the tool on the main menu.')
    else:
        easygui.msgbox('Invalid Password!')
if loginOption == "Create an account":
    username = easygui.enterbox("Choose a username:")
    password = easygui.enterbox("Choose a password:")
    if easygui.ccbox("Are you sure you would like to create your account?") == True:
        record2send = {"username":username, "password":password, 'activated':False}
        coll.insert_one(record2send)
        easygui.msgbox('Your account has been created sucesfully!')
    else:
        easygui.msgbox('No accounts have been created')
if loginOption == "Activate an existing account":
    username = easygui.enterbox("Enter your username:")
    serialKey = easygui.enterbox('Enter your serial number:')
    keyColl = db["SerialNumbers"]
    allKeys = keyColl.find({})
    validKeys = []
    for i in allKeys: validKeys.append(i["serialNumber"])
    if serialKey in validKeys:
        easygui.msgbox('Your serial number has been verified, please wait while we activate your account...')
        coll.update_one({"username":username},{'$set':{"activated":True}})
        easygui.msgbox('Your account has been activated! You can close this windows and sign in now!')
    else:
        easygui.msgbox('Your serial number is invalid!')
