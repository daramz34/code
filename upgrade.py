# #task 1
# name = input("enter in your name: ")
# age = int(input("enter your age: "))
# gpa = float(input("enter your gpa: "))

# print()
# #task 2
# beans = int(input("enter your age "))
# rice = beans + 5
# print(f"your age + 5 is = {rice}years")

# print()
# #task 3
# print("enter 2 numbers")
# ask = int(input())
# two = int(input())

# sum = ask + two
# diff = ask - two
# pro = ask * two
# quo = ask / two

# print(f" your sum is: {sum}, difference: {diff} product: {pro} quotient: {quo}")






# level 2 assessment
# num = int(input("enter a num: "))
# if num > 10:
#     print("high")
# elif num < 5:
#     print("Low")
# else:
#     print("medium")
# print()

# #task 2
# age = int(input("enter your age: "))
# if age >= 18:
#     print("You are an adult")
# elif age < 13 :
#     print("You are a child")
# else: 
#     print("You are a teenager")
# print()

# #task 3
# print("enter 3 numbers")
# three = int(input())
# four = int(input())
# five = int(input())
# high = max(three, four, five)
# low = min(three, four, five)
# print(f"your largest is {high} yours smallest is {low}")






#level 3
#task1
# for x in range(1,11):
#     print(x)



# #task2
# names = []
# count = 0
# while count <5:
#     name = input("enter 5 names: ")
#     names.append(name)
#     count += 1
# print(names)


# for name in names:
#     print(name)





# num = []
# count =0
# while count <5:
#     number = int(input("enter 5 #: "))
    
#     count += 1
#     sum = number + int(sum)
#     avg = sum/5
#     num.append(number)
#     print(num % 2 == 0)





# numbers = []
# count =0
# while count < 5:
#     number = int(input("enter 5 numbers: "))
#     numbers.append(number)
#     count += 1

# total = sum(numbers)
# avg = total/5
# print(total)
# print(avg)


# print("even")
# for x in numbers:
#     if x % 2==0 :
#         print(x)



# names = []
# count = 0
# while count < 5:
#     name = input("enter names ")
#     names.append(name)
#     count += 1
#     for name in reversed(names):
#         print(name)
















# nums = []
# count = 0

# while count < 5:
#     num = int(input("enter numbers: "))
#     nums.append(num)
#     count+=1

# high = max(nums)
# low = min(nums)
# print("Numbers greater than 10:")
# for n in nums:
#     if n > 10:
#         print(n)

# print(f"your highest number is: {high}")
# print(f"your lowest number is: {low}")

    
# dask = [1,2,3,4,5,6,7,8,9,10,11,12]
# for x in dask:
#     num = int(input("enter a number: "))
    
#     mux = x * num
#     print(f"{x} x {num} = {mux}")
#     print()

# num = int(input("Enter a number: "))
# for x in range(1, 13):
#     mux = x * num
#     print(f"{num} x {x} = {mux}")



# #level 4
# #task 1
# fruits = ["apple", "banana", "cherry","mango", "starwberry"]
# print(fruits)
# fruits.insert(0,"grape")

# fruits.remove("mango")
# print(f"updated list : {fruits}")
# print()
# #task 2
# colors = {"red", "blue", "white", "green", "black"}
# print(colors)
# colors.add("pink")
# colors.remove("red")
# print(f"updated list : {colors}")

# print()

# #task3
# coun = ("niger", "nigeria", "usa", "canada","ghana" )
# print(coun)
# print(len(coun))
# print("nigeria" in coun)





#student score analyzer
# count = int(input("enter the number of student: "))
# names = []
# scores = []
# for x in range(count):

#     name = input(f"enter your name: {x+1} ")
#     score = int(input("enter score: "))
#     names.append(name)
#     scores.append(score)

# high = max(scores)
# print(f"highest score is: {high}")
# avg = sum(scores)/count
# print(f"average score is: {avg}")







# practice
# fruits = ["apple", "banana", "cherry"]
# print(fruits)


#adding items to a list
#using for loop
# names = []
# for i in range(5):  # Loop runs 5 times
#     name = input("Enter a name: ")
#     names.append(name)  # Adds each name to the list
# print(names)

#using while loop
# names =[]
# count = 0
# while count < 5:
#     name = input("Enter a name: ")
#     names.append(name)
#     count += 1
# print(names)



# #Processing Items in a List with a Loop
# #print each item using a for loop:
# for name in names:
#     print(name)


# numbers = [2, 5, 8, 11, 14]
# # Print only even numbers
# for n in numbers:
#     if n %2==0:
#         print(n)


# numbers = [2, 5, 8, 11, 14]
# total = sum(numbers)
# avg = total / len(numbers)
# print(f"Sum: {total}, Average: {avg}")




# nums = []
# count = 0
# while count < 5:
#     num=int(input("enter nums: "))
#     nums.append(num)
#     count += 1
# print(nums)
# for num in nums:
#     if num > 10:
#         print()
#         print(f"{num} greater than 10")


#Practice 1: Find Odd Numbers and Their Count
# numbers = []

# for x in range(7):
#     num = int(input("enter numbers: "))
#     numbers.append(num)


# print("Odd numbers:")
# odd_count = 0
# for n in numbers:
#     if n % 2 != 0:
#         print(n)
#         odd_count += 1

# print(f"Total odd numbers: {odd_count}")



#Practice 2: Reverse List and Print
# word= []
# for x in range(5):
#     w = input("enter ab word: ")
#     word.append(w)

# word.reverse()

# print(word)
 




# num = []
# count = 0
# while count < 5:
#     number = int(input("enter 5 #: "))
    
#     count += 1
#     num.append(number)
#     for n in num:
#        if n%2==0:
#          print(n)


# num = []
# # count = 0
# while True:
#    number = int(input("enter a number: "))
#    num.append(number)
#    add = sum(num)
#    if add == -add:
#       break
#    print(f"the sum is {add}")







            
   
       

 # Shopping List Manager
# cart = []

# while True:
#     hi = int(input("1: Add to cart | 2: View cart | 3: Remove from cart | 4: Quit: "))

#     if hi == 4:
#         print("Exiting... Goodbye!")
#         break

#     elif hi == 1:
#         while True:
#             item = input("Enter item (press 'q' to stop): ")
#             if item.lower() == "q":
#                 break
#             cart.append(item)
#         print("Items added to cart.")

#     elif hi == 2:
#         if cart:
#             print("Your cart contains:")
#             for i in cart:
#                 print(f"- {i}")
#         else:
#             print("Your cart is empty.")

#     elif hi == 3:
#         if cart:
#             remove_item = input("Enter the item you want to remove: ")
#             for i, item in enumerate(cart):
#                 if item.lower() == remove_item.lower():
#                     cart.pop(i)
#                     print(f"'{remove_item}' removed from cart.")
#                     break
#             else:
#                 print("Item not found in cart.")
#         else:
#             print("Your cart is empty. Nothing to remove.")

#     else:
#         print("Invalid option. Please choose between 1 and 4.")



#to-do list manager

# todo_list = []

# while True:
#     choice = int(input("1: Add Task | 2: View Task | 3: Mark Done | 4: Quit :  "))
#     if choice == 4:
#         print("bye") 
#         break 
#     elif choice == 1:
#         while True:
#          task = input("Enter task (q to quit): ")
#          todo_list.append(task)
#          if task.lower() == "q":
#             break
#         todo_list.append(task)
#         print("-----Tasks added ----")

#     elif choice == 2:
#               if not todo_list:
#                   print("no tasks")  
#               if todo_list:
#                   for i, task in enumerate(todo_list, 1):
#                      #  status = "done" 
#                      #  sat = "pending"
#                      #  status if task[mark] else sat
                      
#                      #  print(f"{i}: {task["task"]} - {status} ")
#                      print(f"{i}: {task}")
        #incomplete program





























# contacts_books = []
# print("Welcome to your Contact book/file")
# while True: 
#     menu = int(input("1: Add | 2: Search | 3: Delete | 4: Quit: "))

#     if menu == 4:
#         print("Bye")
#         break
    
#     elif menu == 1:
#         while True:
#           import time
#           time.sleep(1)
#           print("Choice 1")
#           time.sleep(1)
#           name = input("Name: ")
#           time.sleep(1)
#           phone = input("Phone number: ")
          
#           while len(phone) < 11 or len(phone) > 11 :
#              if len(phone) < 11 or len(phone) > 11:
#               print("number cant be more or less than 11")
#               phone = input("Phone number: ")
              
#              else: break
#           contacts_books.append([name, phone])
#           leave = input("press enter to save another number else type q : ")
          
#           if leave == "q":
#               break
#         print("------Contacts saved-----")

#     elif menu == 2:
#        import time
#        time.sleep(1)
#        print("Choice 2")
#        search = input("Search name: ")
#        found = False
#        for contact in contacts_books:
#          if contact[0].lower() == search.lower():
#           print(f"Found: Name: {contact[0]}, Phone: {contact[1]}")
#           found = True
#          if not found:
#             print("Contact not found!!")

#     elif menu == 3:
#        import time
#        time.sleep(1)
#        print("Choice 3")
#        delete_name = input("Delete contact: ")
#        found = False
#        for i, contact in enumerate(contacts_books):
#              if contact[0].lower() == delete_name.lower():
#                 removed = contacts_books.pop(i)
#                 print(f"Deleted: {removed[0]}")
#                 found = True
#                 break
#        if not found:
#                       print("Contact not found!!")


    
               
             
        


#In Python a function is defined using the def keyword:
# def my_function():
#   print("Hello from a function")

# #To call a function, use the function name followed by parenthesis:
# my_function()

#arugemts

# def my_function(name):
#   print(name)
# my_function("dara")
# my_function("ani")




#Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

# This way the function will receive a tuple of arguments, and can access the items accordingly:

# def my_function(*kids):
#     print("The youngest child is " + kids[0])
# my_function("Emil", "Tobias", "Linus")







# def greet():
#     print("hello darareaper")

#  #def means you're defining a function.
#  greet is the name of the function.
# () means it doesn’t take any input (yet).

# greet()





#Arguments are values you pass into a function to customize what it does
# def greet(name):
#     print(f"hello {name}")

# greet("darasimi")
# greet("daramz")
# greet("silentshinobi")



#Mini Project 1: Greeting Machine
# def greet(name,age):
#     print(f"Hi {name}, you are {age} years old!!")
# greet("darashinobi", 45)
# greet("daramz", 87)



#🧮 Mini Project 2: Simple Adder
# def add_num(a,b):
#     result = a + b
#     print(f"The sum of {a} and {b} is {result}")

# # add_num(55,4)
# # add_num(383,232)

# def add_num(a,b):
#     result = a + b
#     print(f"The sum of {a} and {b} is {result}")
# a = 7
# b = 13
# add_num(a,b)


#🧮 Mini Project 3: Subtract Two Numbers
# def subtracr_num(a,b):
#     result = a - b
#     print(f"The difference of {a} and {b} is {result}")
# subtracr_num(32,4)


# def subtracr_num(a,b):
#     result = a - b
#     print(f"The difference of {a} and {b} is {result}")
# a = 100
# b = 45
# subtracr_num(32,4)


# def mutliply_num(a,b):
#     result = a * b
#     print(f"The product of {a} and {b} is {result}")
# mutliply_num(66,2)

# def division_num(a,b):
#     result = a / b
#     print(f"The quotient of {a} and {b} is {result}")
# division_num(44,2)




# # 🧮 Mini Project 6: Full Calculator with Menu
# def add(a,b):
#     return a + b
# def subtract(a,b):
#     return a - b
# def multiply (a,b):
#     return a * b
# def division(a,b):
#     if b == 0:
#         return "Error"
#     return a / b
# history = []
# while True:
#     print("\n ------- Simple calcultor part2 -------")
#     print("\n 1. Add. \n 2. Subtract \n 3. Multiply \n 4. Divide \n 5. Show History \n 6. Exit")

#     choice = int(input("Choose an option: "))
     
#     if choice == 5:
#         print("bye")
#         break

#     num1 = float(input("Enter your first number: "))
#     num2 = float(input("Enter second number: "))

#     if choice == 1:
#         result = add(num1,num2)
#         history.append(f"{num1} + {num2} = {result}")
#         print(result)
#     elif choice == 2:
#         result = subtract(num1,num2)
#         history.append(f"{num1} - {num2} = {result}")
#         print()
#     elif choice == 3:
#          result = multiply(num1, num2)
#          history.append(f"{num1} * {num2} = {result}")
#     elif choice == 4:
#        result = division(num1, num2)
#        history.append(f"{num1} / {num2} = {result}")
#     else: 
#         print("invalid")



# #1️⃣ Positional Arguments
# def greet(name, age):
#     print(f"hi {name}, you are {age} years old.")

# greet("dara", 34)



# #2️⃣ Default Arguments
# def greet(name, age= 16):
#     print(f"hi {name}, you are {age} years old")
# greet("dara") # uses default age = 16
# greet("shinobi", 49)  # overrides default with 49


#3️⃣ Keyword Arguments
# Instead of relying on position, 
# you can name the arguments when calling the function.

# def greet(name, age):
#     print(f"hi {name}, you are {age} years old.")
# greet(age = 25, name="dara")
# #You can switch the order because you’re naming them.
# #this makes your code easier to read and less error-prone.



# #Arbitrary Arguments (*args)

# def add_num(*args):
#     total = sum(args)
#     print(f"The total is {total}")
# add_num(2,3,4)
# add_num(3,4,6)

#Arbitrary Keyword Arguments (**kwargs)

# def show_profile(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# show_profile(name="Darasimi", age=21, location="Lagos", hobby="Coding")



# def describe_pet(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
# describe_pet(name= "daisy", animal = "dog", age=4, color="golden white")



# def bulid_profile(**kwargs):
#     print("user profile:")
#     for key, value in kwargs.items():
#         print(f"{key.capitalize()} : {value}")
# bulid_profile(name = "dami", age = 44, hobby="sleeping", location="lagos")


#combo functions
# def combo_function(*args, **kwargs):
#     print("Postional values:", args)
#     print("keyword values: ")
#     for key,value in kwargs.items():
#         print(f"{key} : {value}")
# combo_function(1,2,3, name = "dadsa", mood= "curious")





# if __name__ == "__main__":
#     # This block only runs if you execute this file directly
#     print("Running directly!")


# def add(x,b):
#     return x + b
# def sub(a,b):
#     return a - b

# if __name__ == '__main__':
#     print("Testing calculator:")
#     print("2 + 3 =", add(2, 3))
#     print("5 - 1 =", sub(5, 1))





# def show_all_playlist(playlists):
#     print("\n=== YOUR PLAYLISTS ===")
#     for playlist_name, song in playlists.items():
        







# def main():
#  playlists = {
#         "Favorites": ["Song A", "Song B", "Song C"],
#         "Workout": ["Song X", "Song Y"],
#         "Chill": ["Song P"]
#     }
 

 
#  print("🎵 Welcome to Simple Playlist Manager!")
#  while True:
#         print("\n--- MENU ---")
#         print("1. Show All Playlists")
#         print("2. Add Song to Playlist")
#         print("3. Create New Playlist")
#         print("4. Exit")
        
#         choice = input("Enter choice (1-4): ")
        
#         if choice == "1":
#             show_all_playlist(playlists)
#         elif choice == "2":
#           pass

#         elif choice == "3":
#             pass
#         elif choice == "4":
#             print("🎵 Goodbye!")
#             break
#         else:
#             print("❌ Invalid choice!")






# if __name__ == '__main__':
#      main()


















# def show_books(books):
#     print("=== YOUR BOOK COLLECTION ===")
#     for genre, book in books.items():
#         num_books = len(book)
#         print(f"{genre}: {num_books} books")
#         if len(book) > 0:
#             print(f"  Books: {', '.join(book)}")  # Shows: Book1, Book2, Book3
#         else:
#             print("  (No books)")
#     print("====================================")
        

# def add_book(books):
#     show_books(books)

#     category = input("Enter category name: ")
#     if category in books:
#         book_name = input("Enter book name: ")
#         books[category].append(book_name)
#         print(f"✅ Added '{book_name}' to {category} category")
#     else:
#        print(f"❌ {category} doesn't exist! Create new category.")
        
# def create_new_category(books):
#     new_category = input("Enter new category name: ") 
#     if new_category in books:
#         print("This Category already exists")
#     else:
#         first_book = input(f"Enter First book for {new_category}: ")
#         books[new_category] = [first_book]  
#         print(f"✅ Created new category '{new_category}' with book '{first_book}'")
    

# def search_category(books):
#     category = input("Enter category to search: ")
#     if category in books:
#         print(f"🔍 Books in {category} category:")
#         book_list = books[category]
#         for book in book_list:
#             print(f"-{book}")

        
    

# print("📖 WELCOME TO PERSONAL BOOK COLLECTION MANAGER!📖")

# def main():
#     books = {
#         "Fiction": ["Harry Potter", "Lord of the Rings"],
#         "Science": ["Physics Book", "Chemistry Guide"], 
#         "History": ["World War 2", "Ancient Egypt"]
#     }

#     while True:

        
#         print()
#         print("---Menu---")
#         print("1. Show All Books")
#         print("2. Add Book to Category")
#         print("3. Create New Category")
#         print("4. Search Category")
#         print("5. Exit")

#         choice = input("Enter choice (1-5): ")
#         if choice == "1":
#             show_books(books)
#         elif choice == "2":
#             add_book(books)
#         elif choice == "3":
#             create_new_category(books)
#         elif choice == "4":
#             search_category(books)
#         elif choice == "5":
#             print("Goodbye👋")
#             break
#         else:
#             print("Invalid option!!")




# if __name__ == '__main__':
#     main()



#     # Adding to existing category:
# books[category].append(new_book)  # Adds to end of existing list

# # Creating new category:
# books[category] = [first_book]    # Creates new list with one book

# # Getting a category's books:
# book_list = books[category]       # Copies the list into a variable

# # Pretty display:
# ', '.join(book_list)              # "Book1, Book2, Book3"






# #pizza order manager
# def show_order(orders):
#    print("=" * 40)
#    for customer,order in orders.items():
#       print(f"{customer}  ---> {', '.join(order)}")
#    print("=" * 40)
    
   
# def add_pizza(orders):
#    name = input("Enter customer name: ")
#    if name in orders:
#       pizza_list = orders[name]
#       for pizza in pizza_list:
#          print(pizza)
#       pizza_new = input("Enter pizza to add: ")
#       orders[name].append(pizza_new)
#       print(f"✅ Added {pizza_new} to {name}'s order")
#    else:
#       print("customer hasn't order anything previously❗❗")

# def new_customer(orders):
#    customer = input("Enter new customer: ")
#    if customer in orders:
#       print("This is already an existing customer")
#    else:
#       first_pizza = input("Enter first pizza: ")
#       orders[customer] = [first_pizza]
      
#       print(f"✅ Created order for {customer} with {first_pizza} pizza")



# def find_customer(orders):
#    find = input("Enter customer: ")
#    if find in orders:
#       pizza_list = orders[find]
#       print(f"customer {find} found")
#       for pizza in pizza_list:
#          print(f"pizza - {pizza}")
#    else:
#       print("can't find user")
      

# def customer_receipt(orders):
#    find = input("Enter Customer: ")
#    if find in orders:
#       pizza_list = orders[find]
#       for pizza in pizza_list:
#          print(f"-{pizza}")
#       total = len(pizza_list)
#       print(f"Total pizzas: {total}")
#    else:
#       print("customer hasn't brought any pizza")
      





# def main():
    
 
#  orders = {
#     "John": ["Pepperoni", "Margherita"],
#     "Sarah": ["Hawaiian", "Veggie"],
#     "Mike": ["Supreme"]}
#  while True:
#     print("*" * 40)
#     print("------MENU------")
#     print("*" * 40)
#     print("1. Show All Orders")
#     print("2. Add Pizza to Order")
#     print("3. New Customer Order")
#     print("4. Find Customer")
#     print("5. Customer Receipt")
#     print("6. Exit")
#     print("*" * 40)

#     choice = input("Enter a choice: ")

#     if choice == "1":
#        show_order(orders)
#     elif choice == "2":
#        add_pizza(orders)
#     elif choice == "3":
#        new_customer(orders)
#     elif choice == "4":
#        find_customer(orders)
#     elif choice == "5":
#        customer_receipt(orders)
#     elif choice == "6":
#        print("Goodbye👋")
#        break
#     else:
#        print("Invalid option")




# if __name__ == '__main__':
#     main()




# What is Object-Oriented Programming?
#Think of it like creating blueprints for things, then making actual things from those blueprints.


# Think of a CAR BLUEPRINT (Class)
# Every car has: color, brand, speed
# Every car can: start, stop, accelerate

# From this blueprint, you can make ACTUAL CARS (Objects)
# Car 1: Red Toyota, speed 0
# Car 2: Blue Honda, speed 0  
# Car 3: Black BMW, speed 0




# #Step 1: Creating a Class (Blueprint)
# class Car:  # This is the BLUEPRINT
#     def __init__(self, color, brand):  # Constructor - sets up each car
#         self.color = color    # Each car has a color
#         self.brand = brand    # Each car has a brand  
#         self.speed = 0        # All cars start with speed 0
    
#     def start(self):  # Method - something cars can DO
#         print(f"The {self.color} {self.brand} is starting...")
    
#     def accelerate(self):  # Another method
#         self.speed += 10
#         print(f"Speed is now {self.speed} mph")
    


# #Step 2: Creating Objects (Actual Cars)
# # Make actual cars from the blueprint
# car1 = Car("Red", "Toyota")    # Create first car
# car2 = Car("Blue", "Honda")    # Create second car
# car3 = Car("Black", "BMW")     # Create third car

# # Now each car exists independently!
# print(f"Car 1: {car1.color} {car1.brand}")  # Red Toyota
# print(f"Car 2: {car2.color} {car2.brand}")  # Blue Honda
# print(f"Car 3: {car3.color} {car3.brand}")  # Black BMW












# class student


# making a class
# class Dog:
#     def __init__(self,name,age): #__init__
#         self.name = name ##name and age → act like normal function parameters (temporary variables).
#         self.age = age ##self.name and self.age → are attributes (variables that belong to the object).
#     def bark(self):
#             print(f"{self.name} is barking")
#     def walk(self,distance):
#          print(f"{self.name} walked a distance of {distance}km")


# dog1 = Dog("buddy",5)   # first object
# dog2 = Dog("mams", 44)  #second object
# # print(dog1.name)
# # print(dog2.age)

# dog1.bark() # Output: Buddy is barking! 🐶
# dog2.bark() # Output: mams is barking! 🐶
# dog1.walk(45)





# class Student:
#     def __init__(self,name,grade):
#         self.name = name
#         self.grade = grade
#     def display(self):
#         print(f"Student: {self.name} \n Grade: {self.grade}")

# stud1 = Student("dra",88)
# stud1.display()



# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def bark(self):
#         print(f"{self.name} is barking he is {self.age} years old ")
#     def eat(self, food):
#         print(f"{self.name} is eating {food}") 

# dog1 = Dog("pete", 45)

# dog1.bark()
# dog1.eat("chicken")





# class Student:
#     def __init__(self,name,grade):
#         self.name = name
#         self.grade = grade
#     def display(self):
#         print(f"Student: {self.name}, grade: {self.grade}")

# name = input("Enter student name: ")
# grade = input("ENter student grade: ")

# stud1 = Student(name,grade)
# stud1.display()




# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def rename(self):
#         new_name = input("Enter a new name for the dog: ")
#         self.name = new_name
#         print(f"The dog's name is now {self.name}")





# class Bank_Account:
#    def __init__(self,owner,balance=0):
#       self.owner = owner
#       self.balance = balance
#    def depoit(self,amount):
#       if amount <= 0:
#            print("❌ Deposit must be greater than zero.")
#       else:
#          self.balance += amount
#          print(f"✅ {self.owner} deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
#    def withdraw(self,amount):
#        if amount <= 0:
#             print("❌ Withdrawal must be greater than zero.")
#        elif amount > self.balance:
#             print("⚠️ Not enough funds.")
#        else:
#            self.balance -= amount
#            print(f"💸 {self.owner} withdrew ${amount:.2f}. New balance: ${self.balance:.2f}") 
#    def check_balance(self):
#        print(f"💰 {self.owner}, your current balance is: ${self.balance:.2f}")

           


# print("🏦WELCOME TO PYTHON BANK!🏢")
# name = input("Enter account username: ")
# account = Bank_Account(name)

# while True:
#      print("\n--- Menu ---")
#      print("1. Check Balance")
#      print("2. Deposit Money")
#      print("3. Withdraw Money")
#      print("4. Exit")

#      choice = input("Choose an option(1-4): ")

#      if choice == "1":
#         account.check_balance()
#      elif choice == "2":
#         amount = float(input("Enter amount to deposit: "))
#         account.depoit(amount)
#      elif choice == "3":
#         amount = float(input("Enter amount to withdraw: "))
#         account.withdraw(amount)
#      elif choice == "4":
#         print("👋 Goodbye, thanks for banking with us!")
#         break
#      else:
#         print("❌ Invalid option, try again.")




#mini project of shopping cart
# class Menu:
#     def __init__(self):
#         self.cart = []
        

#     def item(self):
#         item_name = input("Enter item name: ")
#         item_price = float(input("Enter price:$"))
#         self.cart.append((item_name,item_price))
#         print(f"{item_name} has been added to cart!!")
        
#     def remove(self,item):
#         name = input("Enter the item you want to remove: ")
#         for name in self.cart:
#             if item[0] == name:
#              self.cart.remove(item)
#             print(f"{name} has been removed✅")
#             return
#         else:
#             print("This item hasn't been added to cart")

#     def view_cart(self):
#         print()
#         print("Your cart")
#         for item_name, item_price in self.cart:
            
#             print(f"{item_name} --> ${item_price}")

#     def checkout(self):
#         if not self.cart:
#             print("your cart is empty")
#             return
#         total = 0 
#         for item_price in self.cart:
#             total += item_price
#             print(f"Total: ${total:.2f}")
#         print("Thank you for Shopping 🛒")
            




# shopping = Menu()
# def main():
    
#     while True:
#         print("---Shopping Cart Menu🛒---")
#         print("1. Add item🛒")
#         print("2. Remove item")
#         print("3. View cart")
#         print("4. Checkout")
#         print("5. Exit")

#         choice = input("Choose an option: ")
        
#         if choice == "1":
#             shopping.item()
#         elif choice == "2":
#             shopping.remove()
#         elif choice == "3":
#             shopping.view_cart()
#         elif choice == "4":
#             shopping.checkout()
#         elif choice == "5":
#             print("Thank you for Shopping 🛒")
#             break
#         else:
#             print("Invalid option!!!!")

# if __name__ == '__main__':
#     main()








# lists and indexing

# fruits = ["apple", "mango", "banana"]
# #fruits[0] = "apple"
# #fruits[1] = "mango"
# #fruits[2] = "banana"
# #Indexing = grabbing a specific element.

# item = ("apple",200)
# #item[0] → "Apple" (name)
# #item[1] → 200 (price)

# cart = [("Apple", 200), ("Bread", 150)] # list of tuples

# for item in cart:
#     print(item[0], item[1])




# class Dog:
#     # class variable
#     species = "Canine"

#     def __init__(self, name, age):
#         # instance variables
#         self.name = name
#         self.age = age

# # Create dogs
# dog1 = Dog("Buddy", 3)
# dog2 = Dog("Charlie", 5)

# print(dog1.name, dog1.species)  # Buddy Canine
# print(dog2.name, dog2.species)  # Charlie Canine

# # Change class variable
# Dog.species = "Doggo"

# print(dog1.species)  # Doggo
# print(dog2.species)  # Doggo










#oop

# class Bank_Account:
#     def __init__(self,account_holder):
#         self.account_holder = account_holder
        
#         self.inital = 0
#     def deposit(self,amount):
#         amount += self.inital
#         self.inital = amount 
#         print(self.inital)
#         print(f"Deposited ${amount}")
#         return self.inital
#     def withdraw(self,amount):
#         if self.inital >= amount:
#             self.inital -= amount
            
#             print(f"Withdraw ${amount}")
#             return self.inital
#         else:
#             print("Insuffient funds")
#     def get_balance(self):
#         print(f"Balance for {self.account_holder}: ${self.inital}")
    



# account1 = Bank_Account("dara")
# account1.deposit(100)
# account1.withdraw(50)
# account1.get_balance()

# account2 = Bank_Account("bob")
# account2.deposit(200)
# account2.withdraw(300)
# account2.get_balance()









#class variable

# class Bank_Account:
#     total_accounts = 0
    
#     def __init__(self,account_holder):
#         self.account_holder = account_holder
#         self.inital = 0
#         Bank_Account.total_accounts += 1

#     def get_balance(self):
#         print(f"Balance for {self.account_holder}: ${self.inital}")
#     def display_total_accounts(self):
#         print(f"Total accounts created: {Bank_Account.total_accounts}")
    



# account1 = Bank_Account("dara")
# account2 = Bank_Account("bob")

# account1.get_balance()

# account2.display_total_accounts()









# class Student:
#     average_grade = 0.0
#     total_students = 0
#     total_grades_sum =0

#     def __init__(self,name):
#         self.name = name
#         self.grade = 0
#         Student.total_students += 1
        

#     def set_grade(self,grade):
#         Student.total_grades_sum -= self.grade
#         self.grade = grade
#         Student.total_grades_sum += self.grade
#         Student.average_grade = Student.total_grades_sum/Student.total_students
        
        
#     def get_average(self):
#         print(f"Class average grade: {Student.average_grade}")

# s1 = Student("dara")
# s1.set_grade(85)
# s1.get_average()

# s2 = Student("dami")
# s2.set_grade(92)
# s2.get_average()

# s3 = Student("dola")
# s3.set_grade(78)
# s3.get_average()















# # inheritance


# class Vechicle:  #parent
#     def __init__(self,make,year):
#         self.make = make
#         self.year = year
#     def start(self):
#         print("Vechile Starting🚙")
#     def honk(self):
#         print("Beep Beep")
    

# class Car(Vechicle):
#     def __init__(self, make, year,fuel_type):
#         super().__init__(make, year)
#         self.fuel_type = fuel_type

#     def start(self):
#        super().start()
#        print(f"Car starting with {self.fuel_type} fuel")
#     def honk(self):
#         print("Beep Beep")

# class Motorcycle(Vechicle):
#     def __init__(self, make, year,fuel_type):
#         super().__init__(make, year)
#         self.fuel_type = fuel_type
    
#     def start(self):
#         super().start()  
#         print(f"Motorcycle starting with{self.fuel_type} fuel")
    

# bike = Vechicle(make="Honda",year=2025)
# bike.start() 
# bike.honk()
# print(bike.make)
# print(bike.year)



# my_car = Car(make="Tesla",year=2092,fuel_type = "Electric")
# my_car.start()
# my_car.honk()


# cycle = Motorcycle(make="soemthing", year=4343,fuel_type="petrol")
# cycle.start()
# cycle.honk()






#multiple inheritance - a child class inherits from multiple parents



# class Flyer:
#     def fly(self):
#         print("Soaring through the sky!!")
#     def speak(self):
#         print("speak2")
# class Strongman:
#     def lift(self):
#         print("Lifting a car effortlessly!!")
#     def speak(self):
#         print("speak")

# class Superhero(Flyer,Strongman):
#     def __init__(self,name):
#         self.name = name
#     def save_day(self):
#         self.fly()
#         self.lift()
#         print(f"{self.name} saves the day")
    
# hero = Superhero("Superman")
# hero.save_day()
# hero.speak()







# class Vechicle:
#     total_vechicle = 0

#     def __init__(self,make,year):
#         self.make =make
#         self.year = year
#         Vechicle.total_vechicle += 1
#     def move(self):
#         print("Moving on land/sea.")
    
# class Aquatic:
#     def dive(self):
#         print("Diving underwater")

# class Submarine(Vechicle,Aquatic):
#     def __init__(self, make, year,depth):
#         super().__init__(make, year)
#         self.depth = depth
#     def move(self):
#         super().move() # calls vechicle's move #overrides
#         print("Silently through water")
#     def explore(self):
#         self.dive()
#         self.move()
#         print(f"Exploring at {self.depth} meters")

# sub1 = Submarine("USS", 2032, 1200)
# sub1.explore()
# sub2 = Submarine("UeS", 2232, 1000)
# sub2.explore()
# print(f"Total vechicles: {Vechicle.total_vechicle}")
    











# Polymorphism - many forms
# it allows objects of different classees to be treated as objects of a common parent class


# class Shape:
#     def area(self):
#         # raise NotImplementedError("Subclasses must implement area()")  # forces children to override
#         pass
    


# class Circle(Shape):
#     def __init__(self,radius):
        
#         self.radius = radius

#     def area(self):
#        return 3.14 * self.radius * self.radius



# class Rectangle(Shape):
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

# class Triangle(Shape):
#     def __init__(self,base,height):
#         self.base = base
#         self.height = height
#     def area(self):
#         return self.base * self.height / 2
       
# def print_area(shape):
#     print(f"Area: {shape.area()}")
        

# # circle = Circle(2)
# # rectangle = Rectangle(3,2)
# # print(circle.area())
# # print(rectangle.area())
# #OR
# # shapes = [Circle(4),Rectangle(3,4),Circle(34),Rectangle(23,4),Triangle(2,3)]
# # for shape in shapes:
# #     print_area(shape)




# # Duck Typing 

# class PDF:
#     def print_content(self):
#         print("Printing PDF document")

# class WordDoc:
#     def print_content(self):
#         print("Printing Word Document")

# class TextFile:
#     def print_content(self):
#         print("Printing Plain text")

# class Spreadsheet:
#     def print_content(self):
#         print("Printing Spreadsheet data")

# def print_document(doc):
#     doc.print_content() # Duck typing


# documents = [PDF(),WordDoc(),TextFile(),Spreadsheet()]
# for doc in documents:
#     print_document(doc)
    




#Static methods  - they are utility functions inside a class that don't access instance(self) or class(cls)data
# they use @staticmethods decortor


# class Math:
#     @staticmethod
#     def add(x,y):
#         return x +y
    
# # call without instance
# print(Math.add(2,3))


# # call with instance
# m = Math() 
# print(m.add(2,3))




# class Student:
#     average_grade = 0.0
#     total_students = 0 
#     total_grade_sum = 0

#     def __init__(self,name):
#         self.name = name
#         self.grade = 0 
#         Student.total_students += 1

#     @staticmethod
#     def is_valid_grade(grade):
#         return 0 <= grade <= 100
#     def set_grade(self,grade):
#         if not Student.is_valid_grade(grade):
#             print("Invalid grade! Must be 0-100.")
#             return
#         Student.total_grade_sum -= self.grade
#         self.grade = grade
#         Student.total_grade_sum += self.grade
#         Student.average_grade = Student.total_grade_sum / Student.total_students
#     def get_average(self):
#         print(f"Class average grade: {Student.average_grade}")



# # s1 = Student("Dara")
# # s1.set_grade(192)
# # s1.set_grade(78)
# # s1.get_average()







# @property
# it helps you control how attributes are accessed
# Getter - A method marked with @property that lets you accesss a value like an attribute
#Setter - A method marked with @<property_name>.setter to control how a value is set
#Deleter - A method marked with @<property_name>.deleter to control deletion
# class Student:
#     def __init__(self,name,age):
#         self._name = name
#         self._age = age                 # underscore means private


#     @property
#     def age(self):  #getter
#         return self._age
#     @age.setter
#     def age(self,value):
#         if value < 0:
#             print("Age can't be negative!")
#         else:
#             self._age = value


# s = Student("Alice", 30)
# print(s.age)




# class Temperature:
#     def __init__(self,celsius):
#         self._celsius = celsius

#     @property
#     def celsius(self):
#         return self._celsius
    
#     @celsius.setter
#     def celsuis(self,value):
#         if value < -273.15:
#             raise ValueError("Temperature below absolute zero")
#         self._celsius = value


#     @property
#     def fahrenheit(self):
#         return(self._celsius * 9/5) +32
    
# temp = Temperature(25)
# print(temp.celsius)
# print(temp.fahrenheit)



# class BankAccount:
#     def __init__(self,owner,balance):
#         self._owner = owner
#         self._balance = balance
  
#     @property
#     def balance(self):
#         return self._balance
    
#     @balance.setter
#     def balance(self,value):
#         if value < 0:
#             print("Balance can't go negative")
#         else:
#             self._balance = value

#     def deposit(self,amount):
#         self.balance += amount
#         print(f"Deposited {amount}. \n New Balance: {self.balance}")

#     def withdraw(self,amount):
#         if amount > self.balance:
#             print("Insuffient funds")
#         else:
#             self.balance -= amount
#             print(f"Withdraw {amount}. \n New balance: {self.balance}")


# acc = BankAccount("John",900)
# print(acc.balance)
# acc.deposit(300)
# acc.withdraw(199)






#Decorators

# decorator: a function thst tskrd s function and return a modified version

# def shout(func):
#     def wrapper():
#         result = func()
#         return result.upper()
#     return wrapper

# @shout
# def greet():
#     return "Hello"

# print(greet())



# def login_required(func):
#     def wrapper(user_logged_in):
#         if not user_logged_in:
#             print("Please log in first")
#         else:
#             func(user_logged_in)
#     return wrapper


# @login_required
# def view_dashboared(user_logged_in):
#     print("Welcome to your dashboard")


# view_dashboared(True)





# Exception handling
# used to handle errors gracefully instead of crashing
# using try, except,else, and finally
#try: code that might raise an error
#except: Handles specific errors (or general EXCEPTION)
#else: Run if no error occurs
#finally: Always runs
#raise: Throw custom errors




# def divide(a,b):
#     try:
#         result = a/b
#     except ZeroDivisionError:
#         print("cannot divide by zero")
#         return None
#     else:
#         return result
#     finally:
#         print("done")



# print(divide(2,3))
# print(divide(10,0))





# try:
#     x = int(input("Enter a num: "))
#     print(10/x)
# except ZeroDivisionError:
#     print("cant divide by zero!")
# except ValueError:
#     print("Invalid input!  Enter a number.")
# finally:
#     print("DOne")




# def safe_calc():
#     try:
#         num1 = float(input("Enter first number: "))
#         op = input("Enter operator (+ - / *): ")
#         num2 = float(input("Enter second num: "))

#         if op == "+":
#             hi = (num1 + num2)
#             print(hi)
#         elif op == "-":
#             hi = (num1 - num2)
#             print(hi)
#         elif op == "/":
#             hi = (num1 / num2)
#             print(hi)
#         elif op == "*":
#             hi = (num1 * num2)
#             print(hi)
#         else:
#             print("Unknown operator! ")
#     except ZeroDivisionError:
#         print("You can't divide by zero")
#     except ValueError:
#         print("Please only numbers ")


# safe_calc()
        





#File Detection
# it lets you check if a file or folder exist using the os and os.path modules
# os.path.exists(path): check if a file or directory exists (returns T/F)
# os.path.isifle(path): checks if the path is a file
# os.path.isdir(path): check if the path is a directory





# import os

# file = "example.txt"

# if os.path.exists(file):
#     print("File exits")
#     if os.path.isfile(file):
#         print("It is a file")
#     elif os.path.isdir(file):
#         print("IT is a folder")
# else:
#     print("file doesnt exits")


# file finder

# import os
# file = input("Enter file name: ")

# if os.path.exists(file):
#     print("File Exists")
#     if os.path.isfile(file):
#         print("IT a file")
#     elif os.path.isdir(file):
#         print("It is a folder")
# else:
#     print("File not Found")




#Writing File
# txt_data = "Yokoso Watashi no soul society"
# with open("example.txt", "w") as file:
#     file.write(txt_data)

# with open("example.txt", "a") as file:
#     file.write("\n Bankai")



# # note app
# txt_note = input("Enter a note: ")
# with open("file_detect/notes.txt", "w")as file:
#          file.write(txt_note)
# while True:
        

#         end = input("do you want to write another note (y/n): ")
#         if end == "y" :
#              txt_note2 = input("Enter a note: ")
#              with open("file_detect/notes.txt", "a")as file:
#                 file.write( "\n" + txt_note2 )
                
#         elif end == "n":
#             print("bye")
#             break
#         else:
#             print("Invalid option")



#Reading file
# for .txt
# read(): read entire file as a string
# readlines(): reads all lines into a list
# readline(): reads one line at a time






# with open("file_detect/notes.txt", "r") as file:
#     content = file.read()
#     print(content)


# with open("file_detect/notes.txt", "r") as file:
#     lines = file.readlines()
#     for line in lines:
#         print(line.strip())



# #for .txt - .read()
# # for.json - json.load()
# for .csv- csv.reader()





