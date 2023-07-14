from database.mongo import fs , users_collection

class File:
    def __init__(self , filename ):
        self.filename = filename
        
    def savefile(self , file_data):
        saved_file = fs.put(file_data, filename=self.filename)
        return saved_file
    
    def send_file(self):
        existing_file = fs.find_one({ "filename": self.filename })
        return existing_file

    
    def get_all_files():
        files = fs.find()
        files_list = list(files)
        return files_list