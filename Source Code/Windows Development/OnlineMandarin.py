print("Please wait while we sign you into MongoDB..")
import pymongo
import easygui
import pickle
import time
import webbrowser
client = pymongo.MongoClient("mongodb://MangoCoder360:mangomongo321@cluster0-shard-00-00.vckzv.mongodb.net:27017,cluster0-shard-00-01.vckzv.mongodb.net:27017,cluster0-shard-00-02.vckzv.mongodb.net:27017/Cluster0?ssl=true&replicaSet=atlas-e8h9oi-shard-0&authSource=admin&retryWrites=true&w=majority")
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
        #WORK IN PROGRESS
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
