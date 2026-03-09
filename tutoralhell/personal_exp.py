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
        with open(fileName, "a") as file:
            file.write(f"{self.exp} | {self.price}\n")
    
    def add_expense(self):
        self.exp = input("Enter what you want to buy: ")
        self.price = float(input("Enter the price: "))

        


        
        self.save()
    
    def view(self):
        total =0 
        with open(fileName, "r") as file:
            for index, line in enumerate(file, 1):
                print(index, line.strip())

                parts = line.split("|")
                price = float(parts[1])
                total += price
        print("Total: ", total)
            
            # content = file.readlines()
            # total = 0
            # for line in content:
            #     for char in line:
            #         if char.isdigit():
            #             total += float(char)
            
        
            
    

    def delete(self):
        
        
        with open(fileName, "r") as file:
            lines = file.readlines()
            
            for i, line in enumerate(lines, 1):
                print(i, line.strip())
            remove = int(input("Enter the number you want to remove: "))

            if 1 <= remove <= len(lines):
                lines.pop(remove -1)
                with open(fileName, "w") as fw:
                    fw.writelines(lines)
                    print("Deleted")
            
            else:
                print("Invalid number")

                
    
hi = Personal_expense()


while True:
    print("\n === Welcome ===")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. Delete expense")
    print("4. Exit")
    choice = input("Choose an option: ")
    
    if choice == "1":
        hi.add_expense()
        
    elif choice == "2":
        hi.view()
    elif choice == "3": 
        hi.delete()
    elif choice == "4":
        print("Goodbye👋")
        break


                


        

    

