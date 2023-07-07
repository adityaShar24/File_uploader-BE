from database.mongo import files_collection

class File:
    def __init__(self , filename ):
        self.filename = filename
        
    def save_file(self):
        saved_file = files_collection.insert_one({'filename': self.filename}).inserted_id
        return saved_file

    def get_all_files():
        files = files_collection.find()
        files_list = list(files)
        return files_list   