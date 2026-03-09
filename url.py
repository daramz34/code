import random
import string


class URLShortener:
    def __init__(self):
        self.filename = "url.txt"

    
    def make_code(self):
        chars = string.ascii_lowercase + string.digits
        code = ""

        for _ in range(5):
            code += random.choice(chars)
        return code
    
    def add(self, long_url):
        #tried to see if i can verify if the url has https in it

        with open(self.filename, "a") as file:
            file.write(f"{self.make_code()} | {long_url} \n")


    
    
    def get(self, word):
        
        # with open(self.filename, "r") as file:
        #     for line in file:
        #         parts = line.split(" ")
        #         if x in :
        #             if x in file::


        #         print(line)
        with open(self.filename, "r") as fp:
            lines = fp.readlines()

            for row in lines:
                if row.find(word):
                    print(row)
        
        # stop at trying to get a particular word in the txt
bb = URLShortener()
bb.make_code()
# kd = input("Enter long url: ")
# bb.add(kd)
bb.get("ff")
