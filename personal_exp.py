import os
# file_path = "C:\Users\DARAMZ\Desktop\code\expenses.txt"
fileName = "expenses.txt"
# try:
#     file_size = os.path.getsize(file_path)

#     if file_size == 0:
#         print("File is empty")
#     else: 
#         print("File is not empty")
# with open(fileName, "r") as file:
#     if fileName is None:
#         print("bankai")



class Personal_expense:
    def __init__(self):
        self.exp = None
        self.price = None
    

    def save(self):
        with open(fileName, "w") as file:
            file.write(f"{self.exp} | {self.price}")
    
    def add_expense(self):
        exp = input("Enter what you want to buy: ")
        price = input("Enter the price: ")

        self.exp = exp
        self.price = price


        
        self.save()
    
    def view(self):
        with open(fileName, "r") as file:
            for index, value in enumerate(file, 1):
                print(index, value)
            
            if self.price in file:
                print("hhhhhhh")
                # for self.price in file.readlines:
                #     print(self.price)
            else:
                print("byyyyyy")
            # trying to add the total here
        
            
                

                
    
                
                


        

    

hi = Personal_expense()
#hi.add_expense()
hi.view()