from database.mongo import users_collection
from bson.objectid import ObjectId

class User:
    def __init__(self , username , password):
        self.username = username
        self.password = password
        
    def save_users(self):
        user_id = users_collection.insert_one({'username':self.username , 'password':self.password}).inserted_id
        return user_id
    
    def update_user(userId, fileId, filename):
        update_user = users_collection.find_one_and_update(
            {"_id": ObjectId(userId)},
            {"$set": {"fileId": fileId, "filename": filename}},
            return_document=True
        )
        return update_user
    
    def find_by_username(username):
        user = users_collection.find_one({'username': username})
        return user
    
    def get_all_users():
        all_users = users_collection.find()
        users_list = list(all_users)
        return users_list 