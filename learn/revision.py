#age=45
#gpa=6.5
#name="daramz"
#print(f"MY NAME IS {name}")
#print(f"I AM {age} YEARS OLD")
#print(f"my gpa is {gpa} ")


#pineapple=22
#apple=True
#honey=5.3

#honey= int(honey)
#print(honey)


#dola_is_5=False

#if dola_is_5:
  #  print("am an old man")
#else: 
 #   print("iM NOT AN OLD MAN")


#welcome=input("ENTER NAME ")
#age=int(input("how old are you "))



#age = age + 1

#print(f"my name is {welcome}")
#print(f"i am {age} years old")




#friends = 0
#friends -= 2
#print(round(friends))


#calc the length of an arc

#import math
#radius = float(input("enter radius: "))
#b = 2 * math.pi * radius
#n = float(input("enter angle: "))
#arc = n/360 * b
#print(f"output: {arc}")


# enter random number and i will tell u the highest and lowest among them


#print("enter random numbers")
#apple = input()
#banana = input()
#cake = input()

#if apple > banana and apple > cake:
 #   print(f"this is your highest {apple}")
#elif banana> apple and banana > cake:
#    print(f"this is your highest {banana}")
#elif cake > banana and cake > apple:
 #   print(f"this is your highest {cake}")
#else: 
 #   print("idk")
#if apple < banana and apple < cake:
 #   print(f"this is your lowest {apple}")
#elif banana< apple and banana < cake:
 #   print(f"this is your lowest {banana}")
#elif cake <banana and cake < apple:
 #   print(f"this is your lowest {cake}")
#else: 
 #   print("idk")


#Personality Detector
#print("Welcome To My Personality Detector")
#apple = input("Type in your favourite colour to find out your vibe😎 (red, pink, blue, green, purple, brown, white, black, yellow): ")

#if apple == "red":
 #   print ("🔥 You're bold, passionate, and full of energy!")
#elif apple == "pink":
 #   print("🌸 Gentle, romantic, compassionate. You probably wear your heart on your sleeve.")
#elif apple == "blue":
 #   print("🌊 Calm, trustworthy, loyal. You probably value peace and deep connections.")
#elif apple == "green":
 #   print("🍀 Grounded, nurturing, nature-loving")
#elif apple == "purple":
 #   print("🔮  Imaginative, ambitious, mystical")
#elif apple == "brown":
 #   print("🌰Reliable, earthy, sincere, practical, warm-hearted")
#elif apple == "white":
 #   print("🕊️ Peaceful, pure, minimalist")
#elif apple == "black":
 #   print("🕶️ Mysterious, strong, elegant")
#elif apple == "yellow":
 #   print("☀️ Joyful, creative, spontaneous")
#else: 
 #   print("hmmm you have a special colour i like that")



#Checker for a Scholarship
#age = int(input("ENTER YOUR AGE: "))
#gpa = float(input("enter your gpa: "))
#niger = input("are u NIGERIAN or enrolled in a NIGERIAN uni (YES/NO): ")

#if  (age >= 18 and age <= 25) and (gpa > 3.5) and (niger == "YES") :
 #   print("✅ You are eligible for the scholarship!")
#else: 
 #   print("❌ Sorry, you do not meet the eligibility criteria.")



#Speed Checker for Drivers

#speed = int(input("pls enter the speed your vechicle is going rty now: "))
#check = 70

#driver = "PLS SLOW DOWN" if speed > check else "pls continue your journey"
#print(driver)








#Login Authentication System

#user_name = input("ENTER YOUR USERNAME: ")
#password = int(input("ENTER YOUR PASSWORD: "))

#if user_name == "daramz" and password == 5683:
 #   print("WELCOME")
#elif user_name != "daramz" and password == 5683:
 #   print("incorrect username")
#elif user_name == "daramz" and password != 5683:
 #   print("incorrect password")

#else:
 #   print("INVALID USERNAME AND PASSWORD")



# Guess the Secret Number
#import random
#blastoff = int(input("guess the secret number btw 1-10: "))
#random_no = 7
#guess = "yess u got it" if blastoff == random_no else "naaaaa guess again"
#print(guess)

# fish = input("ENTER A 10 DIGITS ND I WILL SUPRISE U ")
# print(fish[::-1])

#Guess the Secret Number PART 2

# blastoff = int(input("guess the secret number btw 1-10: "))
# random_no = 7
# while not blastoff == random_no:
#     print("naaaaa guess again")
#     blastoff = int(input("guess again secret number btw 1-10: "))


# guess = "yess u got it" 
# print(guess)

#Login Authentication System part2

# user_name = input("ENTER YOUR USERNAME: ")
# password = int(input("ENTER YOUR PASSWORD: "))

# if user_name == "daramz" and password == 5683:
#     print("WELCOME")
# while user_name != "daramz" and password != "5683":
#    print("INVALID USERNAME AND PASSWORD")
#    user_name = input("ENTER YOUR USERNAME: ")
#    password = int(input("ENTER YOUR PASSWORD: "))
#    print("WELCOME")



# validate userinput/username part2

# username = input("ENTER A USERNAME: ")
# if len(username) > 12:
#    print("YOUR USERNAME CANT BE MORE THAN 12 CHARACTERS")
#    while len(username) > 12:
#       username = input("ENTER A USERNAME: ")
#       print(f"WELCOME {username}")
# elif not username.find(" ") == -1:
#    print("username cant contain spaces")
#    while  not username.find(" ") == -1:
#       username = input("ENTER A USERNAME: ")
#       print(f"WELCOME {username}")
# if not username.isalpha():
#    print("your username cant contain numbers")
#    while not username.isalpha():
#       username = input("ENTER A USERNAME: ")
#       print(f"WELCOME {username}")


# while True:
#     username = input("ENTER A USERNAME: ")
#     if len(username) > 12:
#         print("YOUR USERNAME CANT BE MORE THAN 12 CHARACTERS")
#         continue
#     if " " in username:
#         print("username cant contain spaces")
#         continue
#     if not username.isalpha():
#         print("your username cant contain numbers")
#         continue
#     break
# print(f"WELCOME {username}")



#Simple Registration System
# while True:
#     username = input("ENTER A USERNAME: ")
#     if len(username) > 12 :
#         print("USERNAME CAN'T BE MORE THAN 12 CHARACTERS")
#         continue
#     if " " in username: 
#         print("USERNAME CAN'T CONTAIN SPACES")
#         continue
#     if not username.isalpha():
#         print("USERNAME CAN'T CONTAIN NUMBERS")
#         continue
#     break
# while True:
#     password = input("ENTER A PASSWORD: ")
#     if len(password) < 6:
#         print("PASSWORD MUST BE AT LEAST 6 CHARACTERS")
#         continue
#     if not any(c.isalpha() for c in password):
#         print("PASSWORD MUST CONTAIN AT LEAST 1 LETTER")
#         continue
#     if not any(c.isdigit() for c in password):
#         print("PASSWORD MUST CONTAIN AT LEAST 1 NUMBER")
#         continue
#     break
# print(f"WELCOME {username} REGISTRATION SUCCESSFUL")


# users = {}

# while True:
#     print("Welcome! Choose an option:")
#     print("1. REGISTER")
#     print("2. LOGIN")
#     print("3. EXIT")
#     option = input("ENTER CHOICE: ")

#     if option == "1":
#         while True:
#             username = input("ENTER A USERNAME: ")
#             if len(username) > 12:
#                 print("USERNAME CAN'T BE MORE THAN 12 CHARACTERS")
#                 continue
#             if " " in username:
#                 print("USERNAME CAN'T CONTAIN SPACES")
#                 continue
#             if not username.isalpha():
#                 print("USERNAME CAN'T CONTAIN NUMBERS OR SYMBOLS")
#                 continue
#             break
#         while True:
#             password = input("ENTER A PASSWORD: ")
#             if len(password) < 6:
#                 print("PASSWORD MUST BE AT LEAST 6 CHARACTERS")
#                 continue
#             if not any(c.isalpha() for c in password):
#                 print("PASSWORD MUST CONTAIN AT LEAST 1 LETTER")
#                 continue
#             if not any(c.isdigit() for c in password):
#                 print("PASSWORD MUST CONTAIN AT LEAST 1 NUMBER")
#                 continue
#             break
#         users[username] = password
#         print(f"WELCOME {username} REGISTRATION SUCCESSFUL")

#     elif option == "2":
#         username = input("ENTER YOUR USERNAME: ")
#         password = input("ENTER YOUR PASSWORD: ")
#         if username in users and users[username] == password:
#             print(f"Login successful! Welcome back, {username}.")
#         else:
#             print("invalid login details")

#     elif option == "3":
#         print("GOODBYE")
#         break

#     else:
#         print("Invalid option. Please try again.")












# contacts_books = []

# while True:
#     menu = int(input("1: Add | 2: Search | 3: Delete | 4: Quit: "))

#     if menu == 4:
#         print("Bye")
#         break

#     elif menu == 1:
#         while True:
#             name = input("Name: ")
#             phone = input("Phone number: ")

#             while len(phone) != 11:
#                 print("Number must be exactly 11 digits.")
#                 phone = input("Phone number: ")

#             contacts_books.append([name, phone])
#             leave = input("Press Enter to store another number or type 'q' to quit: ")
#             if leave.lower() == "q":
#                 break
#         print("------Contacts saved-----")

#     elif menu == 2:
#         search_name = input("Search name: ")
#         found = False
#         for contact in contacts_books:
#             if contact[0].lower() == search_name.lower():
#                 print(f"Found: Name: {contact[0]}, Phone: {contact[1]}")
#                 found = True
#                 break
#         if not found:
#             print("Contact not found!!")

#     elif menu == 3:
#         delete_name = input("Delete name: ")
#         found = False
#         for i, contact in enumerate(contacts_books):
#             if contact[0].lower() == delete_name.lower():
#                 removed = contacts_books.pop(i)
#                 print(f"Deleted: {removed[0]}")
#                 found = True
#                 break
#         if not found:
#             print("Contact not found!!")

















# # quiz game revision

# questions = ( 
#              ("Which planet is known as the Red Planet?: "),

#              ("What is the largest ocean on Earth?: "),

#              ("What is the speed of light?: "),

#              ("Which gas do plants absorb during photosynthesis?: "),

#              ("What is the boiling point of water at sea level?: "),
#              ("Which element has the atomic number 1?: "),
#              ("Who was the first President of the United States?: "),
#              ("What was the name of the ship that sank in 1912 after hitting an iceberg?: "),
#              ("Who is the author of the Harry Potter series?: "),
#              ("Which superhero is known as the 'Man of Steel?': "),
#              ("What is the name of the fictional country in 'Black Panther'?: "),
#              ("What is the capital city of Japan?: "),
#              ("Which continent is the largest by land area?: "),
#              ("Which organ pumps blood throughout the human body?: "),
#              ("What is the largest mammal in the world?: "),
#              ("Which country is known for the Eiffel Tower?: "),
#              ("Which language is primarily spoken in Brazil?: "),
#              ("What is the currency of Japan?: "),
#              )


# options = ( 
#            ("A) Atlantic Ocean  B) Indian Ocean Indian Ocean C) Arctic Ocean D) Pacific Ocean "),

#            ("A) 300,000 km/s B) 150,000 km/s C) 1,000 km/s D) 500,000 km/s "),

#            ("A) Oxygen B) Carbon Dioxide  C) Nitrogen D) Hydrogen "),

#            ("A) 90°C B) 100°C  C) 110°C D) 120°C"),
#            ("A) Helium B) Hydrogen C) Oxygen D) Carbon"),
#            ("A) Abraham Lincoln B) George Washington  C) Thomas Jefferson D) John Adams"),
#            ("A) Britannic B) Titanic  C) Lusitania D) Queen Mary"),
#            ("A) J.R.R. Tolkien B) J.K. Rowling C) George R.R. Martin D) Suzanne Collins"),
#            ("A) Batman B) Superman  C) Spider-Man D) Iron Man"),
#            ("A) Zamunda B) Wakanda C) Genovia D) Latveria"),
#            ("A) Kyoto B) Osaka C) Hiroshima D) Tokyo"),
#            ("A) North America B) Europe C) Africa D) Asia"),
#            ("A) Brain B) Heart C) Lungs D) Liver"),
#            ("A) Giraffe B) Elephant C) Blue Whale D) Hippopotamus"),
#            ("A) Spain B) Italy C) Germany D) France"),
#            ("A) Portuguese B) Spanish C) French D) English"),
#            ("A) Dollar B) Euro C) Yen D) Won")
#            )
# answers = ("B", "D", "A", "B", "B", "B", "B", "B", "B", "A", "A", "D", "D", "B","C", "D", "A", "C",)


# guesses = []
# score = 0
# question_num = 0

# for question in questions:
#     print("**************************")
#     print(question)

#     for option in options[question_num]:
#         print(option)






    
        
    
    


        
        

#sat study tracker

# print("SAT STUDY TRACKER")
# print("\n 1. Add Score\n 2. View averages \n 3. Show weak subjects \n 4. Quit")

# sat = {
   
# }
# while True:
#   choice = int(input("Enter choice: "))

#   if choice == 1:
#     sub = input("Subject: ")
#     score = int(input("Score: "))
#     sat.update({sub : score})
#     print(f"Added score for {sub}")
  
#   if choice == 2:
     
#      for key, value in sat.items():
#       print(f"{key} : {value:.2f}%")

#   if choice == 3:
#     for key, value in sat.items():
#       if value < 80:
#         print(f"WEAK SUBJECT < 80%: {key} : {value}")
#       elif value > 80:
#         print("You have no weak subjects")
#   if choice == 4:
#     print("bye")
#     break
     
  


# #TO-DO LIST
# print("TO-DO LIST")
# print("\n 1. Add Task \n 2. Remove Task \n 3. Show Tasks \n 4. Exit")
# list = [
    
# ]
# while True:
#     to_do = int(input("Enter Choice: "))
    
#     if to_do == 1:
#         task = input("Task: ")
#         hi = list.append(task)
#         print(f"Added: {list}")
#     elif to_do == 2:
#         remove = input("Enter the task you want to remove: ")
#         list.remove(remove)
#         print(f"task successfully removed!!")
#     elif to_do == 3:
#         for tasks in list:
#             print(tasks)
#     elif to_do == 4:
#         print("bye")
#         break
        
        

# #quiz game with leadership board
# print("SAT quiz game")

# questions = (("What is the capital of France?: "),
#            ("What is the chemical symbol for water?: "),
           
#            ("Which artist sang the hit song Shape of You?: "),
#            ("In which year did World War II end?: "),
    
# )
# options = (("Paris"), 
#            ( "H2o"),
           
#            ("Ed Sheeran"), 
#            ( " 1945" ))
# question_num = 0
# score = 0 
# # answers = ("C", "A", "B", "A", "B")
# while True:
#     player = input("Enter player name (q to quit): ")
#     if player == "q":
#         break
#     for question in questions:
#         hi = input(f"Question: {question}").capitalize()
        
#         if hi == options[question_num]:
#             print("correct")
#             score += 1
#         else:
#             print("wrong")
        
    
        
#     question_num += 1
# print(score)
# failed experiment

      

    







# # library 
# books = ["Harry Potter", "Python Basics", "Sherlock Holmes",
#              "Atomic Habits"]
# give = [

# ]
# def available_books():
#     print("-----------------------------------")
#     if len(books) == 0:
#         print("NO books are available")
#     else:
#         print("Available books:")
#         for book in books:
#             print(book)
    

# def borrow_books():
#     print("-----------------------------------")
#     book = input("Enter the book name to borrow: ")
    
#     if book in books:
#         books.remove(book)
#         give.append(book)
#         print(f"You have borrowed '{book}'. ")
#     else:
        
#         print("Book is not avaliable")

# def return_books():
#     print("-----------------------------------")
#     get = input("Enter the book name to return: ")
#     if get in give:
#         give.remove(get) 
#         books.append(get)  
#         print(f"You have returned '{get}'. ")
#     else: 
#         print("You didn't borrow that book.")
    
        
# is_running = True

# while is_running:
#     print("\n------- Library Menu -------")
#     print("1. View available books")
#     print("2. Borrow a book")
#     print("3. Return a book")
#     print("4. Exit")

#     choice = input("Choose an option: ")

#     if choice == "1":
#         available_books()
#     elif choice == "2":
#         borrow_books()
#     elif choice == "3":
#         return_books()
#     elif choice == "4":
#         print("Goodbye!!")
#         is_running = False

#     else:
#         print("Invaild option")





# import random

# def roll_dice():
    
#     return random.randint(1,6)


# print("Welcome to the Dice Rolling Simulator! 🎲")

# is_running = True

# while is_running:
#     print("Rolling the dice......")
#     import time
#     time.sleep(1)
#     result = roll_dice()
#     print(f"You got: {result}🎲🎲")

#     choice = input("Do you want to roll again (Y/N): ").upper()
#     if choice == "Y":
#         continue
#     else: 
#         print("Goodbye!!")
#         is_running = False









# def menu():
#     print("---ATM MENU---")
#     print("1. Check Balance")
#     print("2. Deposit Money")
#     print("3. Withdraw Money")
#     print("4. Exit")

# def check_balance(balance):
    
#     print(f"Your current balance is: ${balance:.2f}")
    
    
# def deposit(balance):
#     amount1 = float(input("Enter the amount to deposit: "))
    
#     if amount1 < 0:
#         print("Amount can't be least than zero")
#         return balance
#     else:
#         balance += amount1
#         print(f"Successfully deposited: ${amount1:.2f}")
#         print(f"Your new balance is: ${balance:.2f}")
#         return balance
    
# def withdraw(balance):
#     amount2 = float(input("Enter the amount to withdraw: "))
#     if amount2 > balance:
#         print("❌ Insufficient funds!")
#     elif amount2 <= 0:
#         print("❌ Enter a valid amount")
#     else:
#         balance -= amount2
#         print(f"✅ Successfully withdrew: ${amount2:.2f}")
#         print(f"Your new balance is: ${balance:.2f}")
#     return balance






# def main():
#     balance = 0
    

#     is_running = True


#     print("=" * 40)
#     print("  WELCOME TO SIMPLE ATM MACHINE")
#     print("=" * 40)

#     while is_running:
#         menu()
#         choice = input("Enter your choice (1-4): ")

#         if choice == "1":
#             check_balance(balance)
#         elif choice == "2":
#             balance=deposit(balance)
#         elif choice == "3":
#             withdraw(balance)
#         elif choice == "4":
#             print("Goodbye!!")
#             is_running = False
#         else: 
#             print("Invalid option")




# if __name__ == '__main__':
#     main()


# def display_all_students(students):
#     print("\n=== ALL STUDENTS ===")
    
#     # Loop through the dictionary
#     for name, grades in students.items():
#         # Calculate average - this works because grades are NUMBERS!
#         average = sum(grades) / len(grades)
#         print(f"{name}: {grades} → Average: {average:.2f}")
    
#     print("=" * 20)

# def add_grade_to_student(students):
#     # First show current students
#     display_all_students(students)
    
#     # Ask which student
#     student_name = input("Enter student name: ")
    
#     # Check if student exists
#     if student_name in students:
#         # Ask for new grade
#         new_grade = int(input("Enter new grade: "))

#         if new_grade < 0 or new_grade > 100:
#                 print("Grade must be between 0 and 100!")
#         else:
#             # Add to their list - THIS IS THE KEY PART!
#             students[student_name].append(new_grade)
#             print(f"✅ Added grade {new_grade} to {student_name}")
#     else:
#         print("Student not found!")

# def add_new_student(students):
#     student_name = input("Enter new student name: ")
    
#     # Check if student already exists
#     if student_name in students:
#         print(f"❌ Student '{student_name}' already exists!")
#     else:
#         first_grade = int(input(f"Enter first grade for {student_name} (0-100): "))
            
#         if first_grade < 0 or first_grade > 100:
#                 print("❌ Grade must be between 0 and 100!")
#         else:
#                 # Create NEW entry in dictionary with a list containing one grade
#                 students[student_name] = [first_grade]
#                 print(f"✅ Added new student '{student_name}' with grade {first_grade}")

# def search_student(students):
#     student_name = input("Enter student name to search: ")
    
#     if student_name in students:
#         grades = students[student_name]
#         average = sum(grades) / len(grades)
#         highest = max(grades)
#         lowest = min(grades)
        
#         print(f"\n🔍 Student Details:")
#         print(f"Name: {student_name}")
#         print(f"Grades: {grades}")
#         print(f"Average: {average:.2f}")
#         print(f"Highest grade: {highest}")
#         print(f"Lowest grade: {lowest}")
#     else:
#         print(f"❌ Student '{student_name}' not found!")


# def main():
#     # Starting data - IMPORTANT: grades are integers, not strings!
#     students = {
#         "John": [85, 92, 78, 88],
#         "Mary": [90, 88, 95, 92]
#     }
    
#     print("Welcome to Grade Calculator!")
    
#     # We'll add the menu loop here next

#     while True:
        
#         print("\n--- MENU ---")
#         print("1. Display All Students")
#         print("2. Add Grade to Student")
#         print("3. Add New Student")
#         print("4. Search Student")       
#         print("5. Exit")   
        
#         choice = input("Enter choice (1-5): ")  
        
#         if choice == "1":
#             display_all_students(students)
#         elif choice == "2":
#             add_grade_to_student(students)
#         elif choice == "3":
#             add_new_student(students)
#         elif choice == "4":            
#             search_student(students)
#         elif choice == "5":              
#             print("Goodbye!")
#             break

# if __name__ == "__main__":
#     main()







# def display_inventory(inventory):
#         print("="*70) 
#         print("                       STORE INVENTORY")
#         print("="*70)
#         print(f"{'Item':<15} {'Price':<10} {'Stock':<8} {'Stock Value':<15} {'Status'}")
#         print("-"*70)
#         for item_name, details in inventory.items():
#          price = details[0]
#          stock = details[1]
#          stock_value = price * stock
#          total_value += stock_value
#          if stock == 0:
#             status = "❌ OUT OF STOCK"
#          elif stock < 10:
#                 status = "⚠️  LOW STOCK"
#          else:
#                 status = "✅ GOOD"
            
#          print(f"{item_name:<15} ${price:<9.2f} {stock:<8} ${stock_value:<14.2f} {status}")
        
#         print("-"*70)
#         print(f"{'TOTAL INVENTORY VALUE:':<44} ${total_value:.2f}")
#         print("="*70)


# def make_sale(inventory,sales):
#       display_inventory(inventory)
#       item_name = ("Enter item to sell: ")

#       if item_name in inventory:
#             current_stock = inventory[item_name][1]
#             price = inventory[item_name][0]
#             if current_stock == 0:
#              print(f"❌ {item_name} is out of stock!")
#              return
#       print(f"Available stock: {current_stock}")
#       print(f"Price per unit: ${price:.2f}")

     
#       quantity = int(input("Enter quantity to sell: "))
#       if quantity <= 0:
#                 print("❌ Quantity must be positive!")
#       elif quantity > current_stock:
#                 print(f"❌ Not enough stock! Only {current_stock} available.")
#       else: 
#             current_stock -= quantity
#             sales[item_name].append(quantity)
#             total_price = price * quantity
#             remaining_stock = inventory[item_name][1]
                
#             print(f"\n✅ SALE COMPLETED!")
#             print(f"Sold: {quantity} {item_name}(s)")
#             print(f"Total: ${total_price:.2f}")
#             print(f"Remaining stock: {remaining_stock}")


# def restock_items(inventory):
#     """Add more stock to existing items"""
#     display_inventory(inventory)
    
#     item_name = input("\nEnter item to restock: ").title()
    
#     if item_name in inventory:
#         current_stock = inventory[item_name][1]
        
        
#         quantity = int(input(f"Enter quantity to add to {item_name} (Current: {current_stock}): "))
            
#         if quantity <= 0:
#                 print("❌ Quantity must be positive!")
#         else:
#                 # Add to current stock
#                 inventory[item_name][1] += quantity
#                 new_stock = inventory[item_name][1]
                
#                 print(f"✅ Added {quantity} {item_name}(s)")
#                 print(f"New stock level: {new_stock}")
                
       
#     else:
#         print(f"❌ {item_name} not found in inventory!")

                
       











# def main():
#     # Store inventory - item_name: [price, quantity_in_stock]
#     inventory = {
#         "Laptop": [899.99, 15],
#         "Mouse": [25.50, 50],
#         "Keyboard": [75.00, 30],
#         "Monitor": [299.99, 20]
#     }

#     # Sales tracking - item_name: [list_of_quantities_sold]
#     sales = {
#         "Laptop": [2, 1, 3],
#         "Mouse": [5, 8, 3],
#         "Keyboard": [4, 2],
#         "Monitor": [1, 2, 1]
#     }


#     print("="*60)
#     print("        WELCOME TO STORE INVENTORY SYSTEM")
#     print("="*60)
    
#     while True:
#         print("\n--- STORE MANAGEMENT MENU ---")
#         print("1. Display Inventory")
#         print("2. Make Sale")
#         print("3. Restock Items")
#         print("4. Sales Report")
#         print("5. Add New Product")
#         print("6. Search Product")
#         print("7. Exit")

#         choice = int(input("\nEnter your choice (1-7): "))
            
#         if choice == 1:
#                 display_inventory(inventory)
                
#         elif choice == 2:
#                 make_sale()
#         elif choice == 3:
#                 pass
#         elif choice == 4:
#                pass
#         elif choice == 5:
#                 pass
#         elif choice == 6:
#                 pass
#         elif choice == 7:
#                 print("\n🏪 Thank you for using Store Inventory System!")
#                 print("Have a great day!")
#                 break
                
#         else:
#                 print("❌ Invalid choice! Please enter a number between 1-7.")


# if __name__ == '__main__':
#     main()






# class GameCharacter:
#     def __init__(self,name,health):
#         self.name = name
#         self.health = health
#     def attack(self):
#         print(f"{self.name} attacks")
#     def take_damage(self, damage):
#         self.health -= damage
#         print(f"{self.name} takes {damage} damage! Health: {self.health}")
  

# hero = GameCharacter("link",100)               #first object
# enemy = GameCharacter("Goblin", 150)            # second object
# # print(hero.name) #print name
# # print(enemy.health)
# hero.attack()
# enemy.take_damage(23)
# hero.take_damage(10)





#Login Authentication System

#user_name = input("ENTER YOUR USERNAME: ")
#password = int(input("ENTER YOUR PASSWORD: "))

#if user_name == "daramz" and password == 5683:
 #   print("WELCOME")
#elif user_name != "daramz" and password == 5683:
 #   print("incorrect username")
#elif user_name == "daramz" and password != 5683:
 #   print("incorrect password")

#else:
 #   print("INVALID USERNAME AND PASSWORD")






# # Login Authentication System 2
# class Username:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

#     def Sign_in(self):
#         welcome = input(f"Create Username: ")
#         self.username = welcome 
        
#         passes = int(input("Create password: "))
#         self.password = passes
        
#         print("Username and password saved")
#     def Login_in(self):
#         hi = input("Enter username: ")
#         bye = int(input("Enter passsword: "))
#         if hi != self.username and bye != self.password:
#             print("Wrong username and password")
#         elif hi != self.username or bye == 5:
#  #   print("incorrect username")
            


# name = None
# passs = None
# user = Username(name,passs)

# print("-----Welcome-----")
# while True:
#     print("1. Sign in")
#     print("2. Login in")
#     print("3. Exit")

#     Authentication = input("Enter choice: ")
    
#     if Authentication == "1":
#         user.Sign_in()
#     elif Authentication == "2":
#         user.Login_in()
#     else:
#         print("Goodbye")
#         break
