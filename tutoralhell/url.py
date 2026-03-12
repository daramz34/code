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
        
        try: 
            with open(self.filename, "r") as file:
                for line in file:
                    parts = line.split("|")
                    code = parts[0].strip()
                    if word == code:
                        url = parts[1].strip()

                        print(url)
                    
                    
        except FileNotFoundError:
            print("No URLs saved yet")

    
    def list(self): 

        with open(self.filename, "r") as file:
            for line in file:
                print(line)


              
bb = URLShortener()




while True:
    print("\n === Welcome ===")
    print("1. Add URL")
    print("2. Get URL")
    print("3. View all")
    print("4. Exit")
    choice = input("Choose an option: ")
    
    if choice == "1":
        kd = input("Enter URL you want to make short: ")
        bb.add(kd)
        
    elif choice == "2":
        dd = input("Enter the URL you want to view: ")
        bb.get(dd)
    elif choice == "3": 
        bb.list()
    elif choice == "4":
        print("Goodbye👋")
        break

    else:
        print("Invalid option")


                


        

    

