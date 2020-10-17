import easygui
import pymongo
bttnChs = ["Get Password By Username"]
tool = easygui.buttonbox("Choose a tool to use", choices = bttnChs)
if tool == "Get Password By Username":
    toFind = easygui.enterbox("Enter a username to search for the corrosponding password")
    client = pymongo.MongoClient("mongodb://MangoCoder360:mangomongo321@cluster0-shard-00-00.vckzv.mongodb.net:27017,cluster0-shard-00-01.vckzv.mongodb.net:27017,cluster0-shard-00-02.vckzv.mongodb.net:27017/Cluster0?ssl=true&replicaSet=atlas-e8h9oi-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client["WindowsApp"]
    collection = db["Users"]
    data = collection.find({"username":toFind})
    for i in data:
        dataFound = i
    msg = str(dataFound)
    easygui.codebox("Here are the results for your search:", "RESULTS", msg)
