from database.mongo import files_collection

class File:
    def __init__(self , filename ):
        self.filename = filename
        
    def save_file(self):
        saved_file = files_collection.insert_one({'filename': self.filename}).inserted_id
        return saved_file
