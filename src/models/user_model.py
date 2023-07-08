from database.mongo import users_collection

class User:
    def __init(self , username , password):
        self.username = username
        self.password = password
        
    def save_users(self):
        user_id = users_collection.insert_one({'username':self.username , 'password':self.password}).inserted_id
        return user_id