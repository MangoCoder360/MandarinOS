import easygui
import pymongo
client = pymongo.MongoClient("mongodb://MangoCoder360:mangomongo321@cluster0-shard-00-00.vckzv.mongodb.net:27017,cluster0-shard-00-01.vckzv.mongodb.net:27017,cluster0-shard-00-02.vckzv.mongodb.net:27017/Cluster0?ssl=true&replicaSet=atlas-e8h9oi-shard-0&authSource=admin&retryWrites=true&w=majority")
bttnChs = ["Get password by username", "Create serial number"]
tool = easygui.buttonbox("Choose a tool to use", choices = bttnChs)
if tool == "Get password by username":
    toFind = easygui.enterbox("Enter a username to search for the corrosponding password")
    db = client["WindowsApp"]
    coll = db["Users"]
    data = coll.find_one({"username":toFind})["password"]
    msg = str(data)
    easygui.codebox("Here are the results for your search:", "RESULTS", msg)
if tool == "Create serial number":
    toCreate = easygui.enterbox('Enter a 1 word serial number to activate')
    db = client['WindowsApp']
    coll = db['SerialNumbers']
    record = {"serialNumber":toCreate}
    coll.insert_one(record)
