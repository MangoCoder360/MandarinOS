print("Please wait while we sign you into MongoDB..")
import pymongo
import easygui
import pickle
import time
import webbrowser
client = pymongo.MongoClient("mongodb://MangoCoder360:mangomongo321@cluster0-shard-00-00.vckzv.mongodb.net:27017,cluster0-shard-00-01.vckzv.mongodb.net:27017,cluster0-shard-00-02.vckzv.mongodb.net:27017/Cluster0?ssl=true&replicaSet=atlas-e8h9oi-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client["WindowsApp"]
coll = db["Users"]
loginOption = easygui.buttonbox("Welcome to MandarinOS Online! We are connected to MongoDB and are ready to start!", choices = ["Login to existing account", "Create an account", "Activate an account"])
if loginOption = "Login to existing account":
    username = easygui.enterbox("Enter your username:")
    password = easygui.enterbox("Enter your password:")
    getData = coll.find({"username":username}) #WORK IN PROGRESS
