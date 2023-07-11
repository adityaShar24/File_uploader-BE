from pymongo import MongoClient
from gridfs import GridFS

MONGO_CONNECTION_STRING = "mongodb+srv://aditya:aditya2004@cluster0.lgjqzvz.mongodb.net/?retryWrites=true&w=majority"

mongoclient = MongoClient(MONGO_CONNECTION_STRING)

Database = mongoclient['File_uplaoder']
fs = GridFS(Database , collection= 'files')
users_collection = Database['Users'] 

try:
    mongoclient.server_info()
    print("Connection to MongoDb Successful!")
except Exception as e:
    print("Failed to Connect" , e)

