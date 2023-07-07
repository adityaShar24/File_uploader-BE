from pymongo import MongoClient

MONGO_CONNECTION_STRING = "mongodb+srv://aditya:aditya2004@cluster0.lgjqzvz.mongodb.net/?retryWrites=true&w=majority"

mongoclient = MongoClient(MONGO_CONNECTION_STRING)

Database = mongoclient['File_uplaoder']
files_collection = Database['files']

try:
    mongoclient.server_info()
    print("Connection to mongoDB successfull!")
except Exception as e:
    print("Failed to connect" , e)