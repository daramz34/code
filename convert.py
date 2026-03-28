import uuid
import json
import os

class PasteBin:
    def __init__(self):
        self.file = "paste.json"
    
    def save(self, content):
        my_uuid = str(uuid.uuid4())
        
        with open(self.file, "a") as f:
            json.dump(f"{content} : {my_uuid}",f, indent=4)
           

    def get(self, paste_id):
        pass

    

bbb = PasteBin()
bbb.save("hello world")