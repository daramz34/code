# #calculator

# user_input = int(input("Enter a number: "))
# operator = input("Enter an operator(+,/,*,-): ")
# user_input2 = int(input("Enter a number: "))

# if operator == "+":
#     result = user_input + user_input2
#     print(f"{result}")
# elif operator == "-":
#     result = user_input - user_input2
#     print(result)
# elif operator == "*":
#     result = user_input * user_input2
#     print(result)
# elif operator == "/":
#     result = user_input / user_input2
#     print(result)
# else:
#     print(f"This'{operator} isn't an operator'")





# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# result = first_name + " " + last_name
# print(f"Your full name is {result}")


#type casting
#str
#bool
#float
#int
# age = 787
# name = "Silent Reaper"

# age = str(8)
# hi = bool(name)
# print(hi)




# name = input("Enter name: ")
# hm = bool(name)
# if hm == False:
# #     print("guyy na")




# # Area of rectangle
# print("Area of a Rectangle")
# length = float(input("Enter your Length: "))
# width = float(input("Enter your width: "))

# results = length * width
# print(f"The Area of the Rectangle is = {results:.10}cm2")

#VARAIBLES DATATYPES, CONDITIONALS, LOOP



# x = range(10)
# print(x)

# #convert to list to display the content of x:
# print(list(x))



# import math

# # print(math.pi)

# e = 4
# a = 9.04
# d = 8.32
# result = math.sqrt(e)
# result = math.ceil(a)
# result = math.floor(d)
# # ceil - rounds a floating number up
# #sqrt- square root
# print(result)





# Slicing Strings
#Slicing
# You can return a range of characters by using the slice syntax.

# Specify the start index and the end index, separated by a colon, to return a part of the string.



# hi = "Silent Reaper"
# print(hi[3:7])



# # Get the characters from the start to position 5 (not included):
# b = "Hello, World!"
# print(b[:5])


# # Get the characters from position 2, and all the way to the end:

# b = "Hello, World!"
# print(b[2:])



# a =  "hello world"
# print(a.upper())
# b = "HELLO WORLD"
# print(b.lower())
# c = "HELLO WORLD"



# conditonal expression
# x if condion else y


# num = 90
# print("HIgh" if num > 50 else"low" )

# # print num if num > 50 else print low


# name =  input("Enter your name: ")
# result = name.isdigit()
# # result =  len(name)
# # print(f"You have '{result}' characters in your name")
# print(result)

# phone_number = input("Enter your phone number: ")
# result = phone_number.count(" ")
# result = phone_number.replace("-", " ")
# print(result)





# hi =  input(" Dont say fuck you; ")
# result = hi.replace("fuck", "good")
# print(result)





# # remember rock paper scissor game
# import random
# option =  ("Rock", "Paper", "Scissors")
# print("---Welcome to My Rock Paper Scissors game---")

# win =  0 
# lose =  0
# is_running = True

# while is_running:
#     choice =  input("Enter a choice (Rock, Paper, Scissors): ").capitalize()
#     computer = random.choice(option)
#     print(f"i chose {computer}")
#     if choice == computer:
#         print("it a tie")
#     elif choice == "Rock" and computer == "Scissors":
#         print("You win!!!")
#         win += 1
#     elif choice == "Scissors" and computer == "Rock":
#         print("You lost!!")
#         lose += 1
#     elif choice == "Rock" and computer == "Paper":
#         print("You lost!!!")
#         lose += 1
#     elif choice == "Paper" and computer == "Rock":
#         print("You win!!!")
#         win += 1
#     elif choice == "Paper" and computer == "Scissors":
#         print("You lose!!!")
#         lose += 1
#     elif choice == "Scissors" and computer == "Paper":
#         print("You win!!!")
#         win += 1
#     elif choice == "Rock" and computer == "Scissors":
#         print("You win!!!")
#         win += 1
#     else:
#         print("Invaild choice")
    
#     if not input("DO you wish to continue (y/n): ").lower() == "y":
#         is_running = False

# print(f"You won {win} times")
# print(f"You lose {lose} times")
# if win > lose :
#     print(f"IN TOTAL YOU WON 🏆")
# elif win == lose:
#     print("IT A DRAW")
# else:
#     print("YOU LOST 😪")
    
    

#indexing

# credit_number =  "1234-5678-9012-3456"
# print(credit_number[2]) 
# print(credit_number[0:4]) # first 4 digits
# print(credit_number[5:9])
# print(credit_number[5:]) # from the 5 digit to the end
# print(credit_number[-1]) #last number
# print(credit_number[-5])
# print(credit_number[::2]) # step- prints every second character in our string
# print(credit_number[::3])


# credit_number =  "1234-5678-9012-3456"
# #printing the last four digit
# last_digits = credit_number[-4:]
# print(f"XXXX-XXXX-{last_digits}")
# credit_number = credit_number[::-1] #resverse the string
# print(credit_number)







# text =  input("Enter a sentence: ")
# print("This is your Sentence backwords")
# print(text[::-1])


# while loops



# Python has two division operators:

# / - Division (returns a float)
# // - Floor division (returns an integer)

# x = 12
# y = 5
# print(x/y)

# print(x//y)

# print(x%y)

# a = 15
# b = 4
# print(a//b)









# # LIST []-  ordered and changeable. DUPLICATES OK
# fruits = ["beans", "cake", "rice"]


# this_list = ["apple", "Banana", "cherry"]
# print(this_list)
# print(len(this_list))   # print number of items in the lists

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list  (this add elements from another list to a list)
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position/index .insert(0,"what you want to change")
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list {in alphabetly order}

# for x in range(1,11)  :
#     print(x)    

# import time
# time.sleep(5)
# print("Time's up!")

# import time 
# times = int(input("Enter how many seconds you wanna wait: "))
# time.sleep(times)
# print("Hi")


# # print(fruits)
# # print(dir(fruits))
# # print(help(fruits))

# fruits[0] = "apple" ## a way you can change items in the list
# print(fruits)
# for fruit in fruits:
#     print(fruit)

# print(len(fruits))
# fruits.insert(2, "noddles")
# fruits.sort()
# print(fruits)

# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)

# thislist =  ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# # thislist.extend(tropical)
# # print(thislist)

# thislist = ["APPLE", "BANANA", "CHERRY", "BEANS"]
# thislist.pop(1)
# print(thislist)


# # If you do not specify the index, the pop() method removes the last item.
# thislist = ["APPLE", "BANANA", "CHERRY", "BEANS"]
# thislist.pop()
# print(thislist)

# # The del keyword also removes the specified index:
# thislist = ["apple", "banana", "cherry"]
# del thislist[1]
# print(thislist)

#The clear() method empties the list.
#The list still remains, but it has no content.
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)


#List comprehension offers a shorter syntax when you want to create 
# a new list based on the values of an existing list.
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)

# mylist = ['apple', 'banana', 'cherry', 'orange', 'kiwi']
# print(mylist[1:4])


# # TO-DO list

# tasks = []
# print("====== Welcome to Your TO-DO list ======")
# # print("1.ADD Task " \
# # " 2.VIEW Task " \
# # " 3.Delete Task"
# # "4. Exit")

# # choice =  input("Enter Your Choice: ")
# while True:
#     print("1.ADD Task " \
#     " 2.VIEW Task " \
#     " 3.Delete Task "\
#     " 4.Exit")
#     choice =  input("Enter Your Choice: ")
#     if choice == "4":
#         print("Goodbye!!👋👋")
#         break
#     elif choice == "1":
#         task =  input("Enter your task: ")
#         tasks.append(task)
#         print("Task successfully added ✅")
#         continue
#     elif choice == "2":
#         for task in tasks:
#             print(task)
#         continue
#     elif choice == "3":
#         delete = input("Enter the task you want to delete: ")
#         if delete not in tasks:
#             print("This task isn't in the list❗❗")
#             continue
#         tasks.remove(delete)
#         print("Successfully Deleted!!✅")
        
        
#     else:
#         print("Invalid chocie!!!")





# # SET - {} unordered and immutable, but Add/Remove OK. No duplicates
# fruits = {"beans", "cake", "rice","coconut"}
# # print(fruits)
# # print(dir(fruits))
# # print(help(fruits))
# fruits.add("pineapple")
# print(fruits)

# note: you cant use indexing on a set
# fruits = {"beans", "cake", "rice","coconut"}
# fruits.add("pineapple")
# fruits.remove("beans")
# fruits.pop() #removes randomly

# print(fruits)

# thisset = {"apple", "banana", "cherry"}

# print("banana" not in thisset)



# #To add items from another set into the current set, use the update() method.
# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}

# thisset.update(tropical)

# print(thisset)
 

# Method	    Shortcut	Description
# add()	        	    Adds an element to the set
# clear()	 	            Removes all the elements from the set
# copy()	 	            Returns a copy of the set
# difference()	 -	    Returns a set containing the difference between two or more sets
# difference_update()	-=	Removes the items in this set that are also included in another, specified set
# discard()	 	        Remove the specified item
# intersection()   	&	Returns a set, that is the intersection of two other sets
# intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
# pop()	 	            Removes an element from the set
# remove()	 	        Removes the specified element
# union()	|	Return a set containing the union of sets
# update()	|=	Update the set with the union of this set and others




# #Guess the Number Game:

# import random
# print("====== Guess the number ========")
# times = 0 
# computer =  random.randint(1,100)

# while True:
#     choice =  int(input("Guess the number im thiking of btw 1-100: "))
     
#     if choice == computer:
#         print("You got it!!!✅")
#         break
#     elif choice > 100:
#         print(f"I said  btw 1-100 your giving me {choice} try again")
#         times += 1
#         continue
#     elif choice < 0 :
#         print(f"I said  btw 1-100 your giving me {choice} try again")
#         times += 1
#         continue
#     elif choice > computer:
#         print("Too high")
#         times += 1
#         continue
#     elif choice < computer:
#         print("Too low")
#         times += 1
#         continue
    
#     else:
#         print("invalid")
# print(f"You guessed {times} times")





# #Tuple = () ordered and unchangebale.  Duplicates Ok. FASTER
# fruits = ("beans", "cake", "rice","coconut")
# print(fruits)
# print(dir(fruits))
# print(help(fruits))
# print(fruits.index("apple"))





# # Shopping cart program
# foods = []
# prices = []
# total = 0

# while True:
#     food = input("ENter a food to buy (q to quit): ")
#     if food.lower() == "q":
#         break
#     else:
#         price = float(input(f"Enter the price of a {food}: $"))
#         foods.append(food)
#         prices.append(price)


# print("====== YOUR CART =======")

# for food in foods:
#     print(food, end=" ")

#     for price in prices:
#         total += price

# print(f"Your total is: ${total}")








# # Palindrome Checker

# word =  input("Enter a word to check if it a palindrome!: ")
# checker =  word[::-1]

# if checker == word :
#     print(f"{word} this word is a palindrome")
# else:
#     print(f"{word} isnt a palindrome")





# dictionary 

# Method	Description
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary


# # quiz game
# questions = (("What is the capital of France?: "),
#            ("What is the chemical symbol for water?: "),
#            ("Which of the following is a Python data type?: "),
#            ("Which artist sang the hit song Shape of You?: "),
#            ("In which year did World War II end?: "),)

# options = (("A) Berlin", "B) Madrid", "C) Paris", "D) Rome"), 
#            ( "A) H2O", "B) O2", "C) CO2", "D) NaCl"),
#            ( "A) Array", "B) List", "C) Stack", "D) Queue"), 
#            ("A) Ed Sheeran", "B) Justin Bieber", "C) Adele", "D) Taylor Swift"), 
#            ( "A) 1942", "B) 1945", "C) 1948", "D) 1950"))
# answers = ("C", "A", "B", "A", "B")
# guesses = []
# score = 0 
# question_num = 0 




# for question in questions:
#     print("------------------")
#     print(question)
#     for option in  options[question_num]:
#         print(option)

#     guess = input("Enter (A,B,C,D)").upper()
#     question_num += 1





# # contact book
# print("=======Welcome to you CONTACT BOOK=======")
# contacts =  {}
# while True:
#     print("1. ADD contact 2. VIEW conacts 3. EXIT")
#     choice =  input("Enter a choice: ")
#     if choice == "3": 
#         print("Goodbye")
#         break
#     elif choice == "1":
#         name =  input("Enter contact name: ")
#         phone_num = input(f"Enter {name} phone number: ")
#         if len(phone_num) > 11 or len(phone_num) < 11:
#             print("Phone number cant be less or greater than 11")
           
#             continue
#         else: 
#             details = {
#             'phone':phone_num
#         }
#         hi = contacts[name] = details

#         print("========= CONTACT ADDED =========")
#         print(hi)

        
#     elif choice == "2":
#         for name, phone_num in contacts.items():
#             phone_num = details['phone']
#             print(f"Name: {name} | Phone: {phone_num}")
    
#     else:
#         print("Invalid choice❌")


        

# #countdown 
# import time
# my_time =  int(input("Enter the time in seconds: "))
# for x in range(my_time,0,-1):
#     seconds = x % 60
#     minutes = int(x/60)%60
#     hour = int(x/3600)
#     print(f"{hour:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)

# print("time's up")




#nested loop
# a loop within another loop




# import random

# number  = random.randint(1,6)

# print(number)

# low = 1
# high = 100

# number = random.randint(low,high)
# print(number)

# options = ("rock", "paper", "scissors")

# print(random.choice(options))


# cards = ["2", "3", "4","5", "6", "7", "8", "9","10", "J", "Q", "K"]






# function
 #  a block of reusagable code

# def happy_birthday():
#     print("YOu are old")
#     print("Happy birthday to you ")
#     print()

# happy_birthday()




# def happy_birthday(name):
#     print("YOu are old")
#     print(f"Happy birthday to you {name}")
#     print()

# happy_birthday("Bro")

# any data you send to a function is called an argument ("bro")
# parameter is a varaiable usee within a function(name)

# def happy_birthday(name,age):
#     print("YOu are old")
#     print(f"Happy birthday to you {name}")
#     print(f"You are {age} yrs old")
#     print()


# happy_birthday("Daramz", 18)





# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")


# display_invoice("Daramz", 7000, "1/01")  



# return = statement used to end a function
#           and send a result back to the caller

# def add(x,y):
#     z = x + y
#     return z

# def sub(x,y):
#     z = x - y
#     return z

# print(add(2,3))
# print(sub(5,8))




# def create_name(first, last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last


# full_name = create_name("silent", "reaper")

# print(full_name)




# default arguments
# def net_price(list_price,  discount=0, tax=0.05):
#     return list_price * (1 - discount) * (1 + tax)

# print(net_price(500))



# import time

# def count(end, start=0):
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)

#     print("Done")

# count(10)


# defaults arguments should be after postional arguments





# keyword arguments

# def hello(greeting, title, first, last):
#     print(f"{greeting}  {title} {first} {last}")


# hello("Hello", title="Mr.",last="code", first="SPongebob" )

# # postional argument follows keyword argument




# def get_phone(country,area,first,last):
#     return f"{country}-{area}-{first}-{last}"

# phone_num = get_phone(country=23, area=213, first=234, last=673)
# print(phone_num)



# Arbitrary
# *args-arguments-tuple
# **kwargs-keywords arguments-dictionary
 

# def add(*args):  # the args does matter mostly "*"
#     total = 0
#     for arg in args:
#         total += arg
#     return total
    
# print(add(1,2,3))


# def print_address(**kwargs):
#     for value in kwargs.values():
#         print(value)
#     print(" ")
#     for key in kwargs.keys():
#         print(key)
#     print(" ")
#     for key,value in kwargs.items():
#         print(f"{key} : {value}")

# print_address(street="134 fake st.", city="lagos",state="ejibgo",zip="34344",)



# def shipping_label(*args,**kwargs):
#     for arg in args:
#         print(arg, end= " ")
#     print()

#     if "apt" in kwargs:
#      print(f"{kwargs.get('street')} {kwargs.get('apt')}")
#     else:
#        print(f"{kwargs.get('street')}")

#     print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}  ")

# shipping_label("DR.", "SPonge", "Pants", "III",
#               street="134 fake st. ",
#               apt="#100",
#                 city="lagos",
#                 state="ejibgo",
#                 zip="34344")






# my_dict = {"A": 1, "B":2, "C":3}

# for value in my_dict.values():
#     print(value)

# print()

# for key in my_dict.keys():
#     print(key)
# print()

# for key, value in my_dict.items():
#     print(f"{key} ----- {value}")





# word = "APPLE"


# letter = input("Guess a letter in the secret word: ").upper()


# if letter in word:
#     print(f"There is a {letter}")
# else:
#     print(f"{letter} was not found")



# crerate a game that the user will guess the numbers of letters that word have then guess the word





# word = "key"


# hi = len(word)




# while True:
#     guess = int(input(f"Guess the number of letters in the secret words: "))
#     if guess != hi:
#         print("Wrong❌  the letter is btw 1-10: ")
#         continue

#     elif guess == hi:
        
#         print(f"Correct✅")
#         print(f"Now guess the letters in the word")
#         letter = input("   ")


#         if letter in word:
#             print(f"'{letter}' is in the word")
#         else:
#             print(f"{letter} not in the word")
#             continue
#     else:
#         print("")
#         break










# grades = {"Sandy":"A",
#           "Squidward" : "B",
#           "Spongebob" : "C",
#           "Patrick" : "D"
# }

# student = input("ENter the name of a student: ").capitalize()

# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} was not found")








# List comprehension 


# [expression for value in iterable if condition]


# doubels = [  x*2 for x in range(1,11,)]

# print(doubels)






# #match-case statemnt

# def day_of_week(day):
#     match day:
#         case 1:
#             return "IT sunday"
        
#         case 2:
#             return "IT monday"
        
#         case 3:
#             return "u know jare"
        
#         case _:  # like an else statement
#             return "it not there jare"


# print(day_of_week(5))




# note for an OR statement in match-case statement =  |





# import math
# print(math.pi)


#or


# import math as m

# print(m.pi)

# or


# from math import pi
# print(pi)





# import example

# result = example.pi
# result2 = example.square(5)
# result3 = example.area(7)

# print(result, result2, result3)




# # scope resoultion
# #local
# def func1():
#     a = 1
#     print(a)

# def func2():
#     b = 2
#     print(b)

# func1()
# func2()



# # enclosed
# def func1():
#     x = 1
    

#     def func2():
       
#         print(x)
#     func2()

# # enclosed one will print first if remove the local one wil print

# func1()



# #global
# def func1():

#     print(x)

# def func2():
    
#     print(x)

# x= 3
# func1()
# func2()



# #bult-in

# from math import e

# def func1():
#     print(e)

# e = 3

# func1()


# note it follows this order LEGB Local - Enclosed - Global - Bult-in



# def fav_food(food):
#     print(f"Your fav food is - {food}")

# def main():
#     print("this is script")
#     fav_food("pizza")
#     print("bye")

# if __name__ == '__main__':
#     main()



# OOP

# class Car:
#     def __init__(self, model, year, color, for_sale):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale =  for_sale
    
# car1 = Car("BMW", 2023, "red", True)
# car2 = Car("Charger", 2025, "yellow", False)
# print(car1.model)
# print(car1.color)
# print()
# print(car2.year)
# print(car2.for_sale)



# class Car:
#     def __init__(self, model, year, color, for_sale):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale =  for_sale

#     def drive(self):
#         print(f"You drive the {self.color} {self.model}")
    
#     def stop(self):
#         print(f"You stopped the {self.color} {self.model}")
    
#     def describe(self):
#         print(f"{self.year} {self.color} {self.model}")


    
# car1 = Car("BMW", 2023, "red", True)
# car2 = Car("Charger", 2025, "yellow", False)
# # print(car1.model)
# # print(car1.color)
# # print()
# # print(car2.year)
# # print(car2.for_sale)
# car1.stop()
# car2.drive()

# car1.describe()



# class Student:

#     class_year =2029   # class variable
#     no_student = 0 
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         Student.no_student += 1

    
    
    


# stud1  = Student("Daramz", 72)
# stud2 = Student("dark", 64)
# stud3 = Student("Sandy", 38)
# # print(stud1.name)
# # print(stud2.age)

# # print(stud1.class_year)
# # print()
# # print(Student.class_year)


# print(Student.no_student)

# print(f"My graduating class of {Student.class_year} has {Student.no_student}")
# print(stud1.name)
# print(stud2.name)
# print(stud3.name)



# #inhertiance


# class Animal:
#     def __init__(self,name):
#         self.name = name
#         self.is_alive = True
    
#     def eat(self):
#         print(f"{self.name} is eating")
    
#     def sleep(self):
#         print(f"{self.name} is sleeping")


# class Dog(Animal):
#     def speak(self):
#         print(f"WooF")

# class Cat(Animal):
#     pass

# class Mouse(Animal):
#     pass

# dog = Dog("Daisy")
# cat = Cat("rose")
# rat = Mouse("mickey")


# print(dog.name)
# print(dog.is_alive)
# cat.eat()
# rat.sleep()
# dog.speak()


# # super()
# class Shape:
#     def __init__(self, color, is_filled):
#         self.color = color
#         self.is_filled = is_filled
    
#     def describe(self):
#         print(f"This is a Shape, it is color {self.color}")


# class Circle(Shape):
#     def __init__(self,color,is_filled, radius):
#         super().__init__(color, is_filled)
#         self.radius = radius
    
#     def des(self):
#         super().describe()

# class Square(Shape):
#     def __init__(self,color,is_filled, width):
#        super().__init__(color, is_filled)
#        self.width = width
    
#     def des(self):
#         super().describe()


# # we see the class circle and square have two things in common that is the color and filled.

# circle = Circle(color="red", is_filled=True, radius=5)  # using keyword arg
# square = Square("blue", False, 7) # using default arg

# print(circle.color)
# print(circle.is_filled)
# circle.des()
# print()
# print(square.color)
# square.des()






# # #polymorphism

# from abc import ABC, abstractmethod
# class Shape:
#     @abstractmethod
#     def area(self):
#         pass



# class Circle(Shape):
#     def __init__(self,radius):
#         super().__init__()
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2



# class Square(Shape):
#     def __init__(self,side):
#         super().__init__()
#         self.side = side
    
#     def area(self):
#         return self.side ** 2


# shapes = [Circle(3), Square(4)]
# for shape in shapes:
#     print(shape.area())









# class Person:
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name
    
#     def display_info(self):
#         print(f"Name: {self.name}, Age: {self.age}", end=", ")
    

# class Teacher(Person):
#     def __init__(self, age, name,subject):
#         super().__init__(age, name)
#         self.subject = subject
    
#     def display_info(self):
#         super().display_info()
#         print(f"Subject: {self.subject}")
        


# class Student(Person):
#     def __init__(self, age, name,gpa):
#         super().__init__(age, name)
#         self.gpa = gpa
    
#     def display_info(self):
#         super().display_info()
#         print(f"GPA: {self.gpa}")


# student1 = Student(name="ALice", age=11, gpa=3.5)
# teacher1 = Teacher(name="Mr.Ben", age=30, subject="Chemistry")



# print("------- School DIrectory  -------")

# student1.display_info()
# teacher1.display_info()




# class Member:
#     registration_fee = 50
#     total_members = 0

#     def __init__(self,name):
#         self.name = name

#         Member.total_members += 1
    
#     def display_info(self):
#         print(f"Username: {self.name} ")
#         print(f"registration fee = ${Member.registration_fee}")


# print("----- Registrating Memebers")
# member1 = Member("Alice")
# member2 = Member("Ben")
# member3 = Member("Qwen")

# print("---- individual info -----")
# member1.display_info()
# member2.display_info()


# print(f"total memebers = {Member.total_members}")
       

        
# print("Inflation hit soooo registration fee is increased to 60")
# Member.registration_fee += 25

# member3.display_info()




# class PowerSource:
#     def plugin(self):
#         print("Devivce is now connected")


# class InternetConnected:
#     def connect_to_wifi(self):
#         print("Connecting to the home network")
    

# class SmartCamera(PowerSource, InternetConnected):
#     def record(self):
#         print("Security camera is now recording")



# print("----- Setting up smart Camera ------")

# my_cam = SmartCamera()
# my_cam.connect_to_wifi()
# my_cam.plugin()
# my_cam.record()



# class Vehcile:
#     total_vechicle = 0

#     def __init__(self, brand, model ):
#         self.brand = brand
#         self.model = model
        
#         Vehcile.total_vechicle += 1
    
    


# class GasEngine:
#     def fuel_up(self):
#         print("filling the tank with gas")


# class ElectricMotor:
#     def charge(self):
#         print("Charging the battery")


# class HybridCar(Vehcile,GasEngine,ElectricMotor):
#     def __init__(self, brand, model, battery_life):
#         super().__init__(brand, model)
#         self.battery_life = battery_life
    
#     def display_stats(self):
#         print(f"------ {self.brand} {self.model} -------")
#         print(f"Battery: {self.battery_life}%")
    


# car1 = HybridCar("Toyota", 2023, 90)

# car1.fuel_up()
# car1.charge()

# print(f"Total inventory in dealership: {Vehcile.total_vechicle}")







#Ducktyping


# class Animal:
#     alive =  True


# class Dog(Animal):
#     def speak(self):
#         print("WOOF")


# class Cat(Animal):
#     def speak(self):
#         print("meow")

# class Car:
#     alive = False
#     def speak(self):
#         print("Honk")

# animals = [Dog(), Cat(),Car()]

# for animal in animals:
#     animal.speak()
#     print(animal.alive)



# #static method
# class Employee:
#     individual = 0
#     def __init__(self,name, position):
#         self.name = name
#         self.position = position
#         Employee.individual += 1

#     def get_info(self):
#         return f"{self.name} = {self.position}"
    

#     @staticmethod
#     def is_valid_postion(postion):
#         valid_postion = ["Manager", "Cashier", "Cook", "Janitor"]
#         return postion in valid_postion
    
# emplooyee1 = Employee("EUGNEE", "Manager")
# emplooyee2 = Employee("bob", "cook")
# emplooyee3 = Employee("squid", "cashier")

#calling the staicmethod
# print(Employee.is_valid_postion("Cook"))

# print(emplooyee1.get_info())
# print(emplooyee2.get_info())
# print(emplooyee3.get_info())

# print(Employee.individual)




# # class method
# class Student:
#     count = 0
#     total_gpa = 0
#     def __init__(self,name,gpa):
#         self.name = name
#         self.gpa = gpa
#         Student.count += 1
#         Student.total_gpa += gpa
    
#     def get_info(self):
#         return f"{self.name} {self.gpa}"
    

#     @classmethod
#     def get_count(cls):
#         return f"Total number of students: {cls.count}"
    
#     @classmethod
#     def get_average(cls):
#         if cls.count == 0:
#             return 0 
        
#         else:
#             return f"Average gpa = {cls.total_gpa / cls.count:.2f}"
    

# stud1 = Student("Bod", 3.2)
# stud2 = Student("Sandy", 4.0)
# #calling the class method
# print(Student.get_count())
# print(Student.get_average())


# magic methods - dunder methods(double underscore)

# class Book:
#     def __init__(self, title, author, num_pages):
#         self.title = title
#         self.author = author
#         self.num_pages = num_pages

#     def __str__(self): # returning a string representation of the object
#         return f"{self.title} by {self.author}"
    
#     def __eq__(self, other): # checking if the books has the same title and author #so creating two new books with the same title and author
                                
#         return self.title == other.title and self.author == other.author
    
#     def __lt__(self, other):
#         return self.num_pages < other.num_pages
    
#     def __gt__(self, other):
#         return self.num_pages > other.num_pages
    

#     def __add__(self, other):
#         return f"{self.num_pages + other.num_pages} pages"
    
#     def __contains__(self, keyword):
#         return keyword in self.title or keyword in self.author
    
#     def __getitem__(self, key):
#         if key == "title":
#             return self.title
        
#         elif key == "author":
#             return self.author
        
#         elif key == "num_pages":
#             return self.num_pages
        
#         else:
#             return f"Key '{key}' was not found"
    

    
    



# book1 = Book("The hobbit", "J.R.R", 310)
# book2 = Book("Harry potter", "J.K", 223)
# book3 = Book("LIon king", "C.S", 490)

# book4 = Book("Game of Thrones", "D_ramz", 892)
# book5= Book("Game of Thrones", "D_ramz", 921)

# print(book2)
# print(book4 == book5)

# print(book2 < book1)
# print(book4 > book3)

# print(book4 + book1)

# print("LIon" in book3)

# print(book1["title"])
# print(book3["author"])
# print(book4["num_pages"])
# print(book5["audio"])




# #racing game
# class Vechicle:
#     def __init__(self,brand, vechicle):
#         self.brand = brand
#         self.vechicle = vechicle

#     def go(self):
#         print(f"The {self.brand} {self.vechicle} is driving fast")
# class Car(Vechicle):
#     def __init__(self, brand, vechicle):
#         super().__init__(brand, vechicle)
    
#     def go(self):
#         return super().go()


# class Motorcycle(Vechicle):
#     def __init__(self, brand, vechicle):
#         super().__init__(brand, vechicle)

    


# class Bicycle(Vechicle):
#     def __init__(self, brand, vechicle):
#         super().__init__(brand, vechicle)

# class PizzaDelivery:
#     def go(self):
#         print("The pizza delivery guy is running")


# car1 = Car("Tesla", "car")
# bike = Motorcycle("Harley", "bike")
# cycle = Bicycle("giant", "cycle")
# pizza = PizzaDelivery()


# racers = [car1, bike, cycle, pizza]
# print("====== the race start now ======")

# for racer in racers:
#     racer.go()



# # bank manager

# class BankAccount:
#     interest_rate = 0.03

#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

    
#     @staticmethod
#     def is_valid_transaction(amount):
#         return amount > 0
    
    


#     def deposit(self,amount):
#         if BankAccount.is_valid_transaction(amount):
#             self.balance += amount
#             print(f"Deposited ${amount} for {self.owner}")
#         else:
#             print("❌ invalid deposit amount!")


#     @classmethod 
#     def change_rate(cls, new_rate):
#         cls.interest_rate = new_rate
#         print(f"Bank Alert: Interest rate updated to {cls.interest_rate * 100}")


# user1 = BankAccount("Alice", 1000)
# user2 = BankAccount("Bob", 2000)
# print(BankAccount.is_valid_transaction(500))
# user1.deposit(500)

# print(f"Alice's old rate: {user1.interest_rate}")
# BankAccount.change_rate(0.05)
# print(f"Alice's New rate: {user1.interest_rate}")
# print(f"Bob's New rate: {user2.interest_rate}")









# class Starship:
#     total_ships =0
#     def __init__(self, name, firepower):
#         self.name =  name
#         self.firepower = firepower
#         Starship.total_ships += 1

#     def __str__(self):
#         return f"Ship: {self.name} | Power: {self.firepower}"
    
#     def __gt__(self,other):
#         return self.firepower > other.firepower 
    


#     @staticmethod
#     def is_safe_temp(temperature):
#         return -100 <= temperature <= 100
    
#     @classmethod
#     def get_fleet_status(cls):
#         return f"Total ship = {cls.total_ships}"
    

# class Fighter(Starship):
#     def mission(self):
#         print(f"Attacking the enemy fleet 💥")


# class Cargoship(Starship):
#     def mission(self):
#         print("Transporting supplies to colonies 📦")

# class AlienUFO:
#     def mission(self):
#         print("Observing from the shadows... 🛸")



# ship1= Fighter("X-Wing", 500)
# ship2 = Cargoship("Falcon", 200)
# ufo = AlienUFO()

# print("----- System check -----")
# print(f"IS 50c safe for landing? {Starship.is_safe_temp(50)}")

# print()
# print(ship1)
# print(f"Is {ship1.name} stronger than {ship2.name}? {ship1 > ship2}")

# fleets = [ship1, ship2, ufo]
# print()
# for fleet in fleets:
#     fleet.mission()

# print("")
# print(Starship.get_fleet_status())





# @Property getter - read , setter - write, deleter - delete


# class Rectangle:
#     def __init__(self, width, height):
#         self._width = width # meant to be used in the class
#         self._height = height
    
#     @property
#     def width(self):
#         return f"{self._width:.1f}cm"

#     @property
#     def height(self):
#         return f"{self._height:.1f}cm"
    
#     @width.setter
#     def width(self, new_width):
#         if new_width > 0:
#             self._width = new_width
#         else:
#             print("Width must be greater than zero")

    
#     @height.setter
#     def height(self, new_height):
#         if new_height > 0:
#             self._height = new_height
#         else:
#             print("Height must be greater than zero")

#     @width.deleter
#     def width(self):
#         del self._width
#         print("Width has been deleted")

#     @height.deleter
#     def height(self):
#         del self._height
#         print("Height has been deleted")


    


# rectangle = Rectangle(3,4)
# rectangle.width = 7
# rectangle.height = 39
# print(rectangle.width)
# print(rectangle.height)
# del rectangle.width
# del rectangle.height



# # decorator
# def add_sprinkles(func):
#     def wrapper(*args, **kwargs):
#         print("** You add sprinkles **")
#         func(*args, **kwargs)
#     return wrapper

# def add_fudge(func):
#     def wrapper(*args, **kwargs):
#         print("You add fudge")
#         func(*args, **kwargs)
#     return wrapper

# @add_sprinkles
# @add_fudge
# def get_ice_cream(flavour):
#     print(f"here is your {flavour} ice cream 🍧")

# get_ice_cream("Strawberry")



# # # # exception an event that interrupts the flow of a program
# # # (ZeroDivisionError, TypeError, ValueError)
# # 1. try  2. except 3. finally

# try:
#   number = int(input("ENter a number: "))
#   print(1 / number)
# except ZeroDivisionError:
#   print("You cant divdie by zero IDIOT")
# except ValueError:
#   print("Enter only numbers pls")
# except Exception:
#   print("Something went wrong")
# finally:
#   print("Do some clean up")




# def device_log(func):
#     def wrapper(*args, **kwargs):
#         print("[LOG]: Accessing device system...")
#         return func(*args, **kwargs)
#     return wrapper

# class SmartLight:
#     def __init__(self, brightness):
#         self._brightness = brightness

#     @property
#     def brightness(self):
#         return self._brightness
    

#     @brightness.setter
#     def brightness(self, value):
#         if value > 100:
#             print("Too bright")
#             self._brightness = 100
#         elif value < 0 :
#             print("Too dark ")
#             self._brightness = 0
#         else:
#             self._brightness = value

#     @device_log
#     def turn_on(self):
#         print("THe light is now on")


    
# my_light = SmartLight(50)
# my_light.turn_on()

# my_light.brightness= 4004


# # create a bank account to pay sch fee buh your account starts off with 0 buh with each question answered you gain more money to be able to pay your sch fee
# # it shows the amount or percentage of sch fee paid 

# class Bowen_Account:
#     balance = 0
#     sch_fee = 1400000
#     gain = 0
#     questions = None
#     options = None
#     answers = None
#     question_num = 0
#     guessess = None

#     def __init__(self,user_name):
#         self.user_name = user_name
        
        
#         Bowen_Account.balance += 1000
    

#     def show_account(self):
#         print("====== Welcome To Bowen Account ======")
#         print(f"{self.user_name.upper()} has a total balance of: {Bowen_Account.balance} for signing in")
#         print()
#         print(f"Your sch fee is {Bowen_Account.sch_fee:,}")
#         print()
#         print("inorder To gain money to be able to pay for you sch fee you have to gain points/cash by answering questions")


    
#     def quest(self):
    
#         Bowen_Account.questions = (
#                         ("Speaking and writing are ______  skill"),
#                         ("Any situation that requires listening is labelled_________"),
#                          ("A dictionary written basically for translation of languages is  callled _______"),
#                          ("The full meaning of CAT is _______")
#                          )
#         Bowen_Account.options = (
#                         ("(A) Productive", "(B) Adaptation",  "(C) Adaptive",  "(D) Logical"), 
#                         ("(A) Note-making", "(B) Note-made", "(C) Note-taking",   "(D) Note-taken"),
#                        ("(A) Language",  "(B) Bilingual", "(C) Subject",  "(D) Electronic"),
#                        ("(A) Content Area Textbook",   "(B) Culture Area Textbook",  "(C) Criminal Area textbook",   "(D) Comic Area Textbook"),
                         
#                          )
#         Bowen_Account.answers =  ("A", "C", "B", "A" )
#         Bowen_Account.guessess = []
#         Bowen_Account.question_num = 0

#         for question in Bowen_Account.questions:
#              print("-----------------")
#              print(question)

#              for option in Bowen_Account.options[Bowen_Account.question_num]:
#                  print(option, end=" ")
                 
#                  print()
    
#              guess = input("Enter an option: ").upper()
#              Bowen_Account.guessess.append(guess)
#              if guess == Bowen_Account.answers[Bowen_Account.question_num]:
#                 Bowen_Account.gain += 300000
#                 print(f"Correct you have gained $100000")
#              else:
#                 print("Wrong")
#                 print(f"{Bowen_Account.answers[Bowen_Account.question_num]} is the correct answer")


#              Bowen_Account.question_num += 1
             
            
#     def total_balance(self):
#         Bowen_Account.balance = Bowen_Account.gain
#         print(f"Total balance is: ${Bowen_Account.balance:,}")

#         #  Bowen_Account.sch_fee - Bowen_Account.balance 
#         half =  Bowen_Account.sch_fee * 0.50
#         if Bowen_Account.balance > half:
#             print("You Balance reached 50 percent of the sch fee")
#         else:
#             print("You Balance didnt reach 50 percent of the sch fee")

        
            

    


# name = input("Enter name : " )

# user1 = Bowen_Account(name)
# user1.show_account()
# user1.quest()
# user1.total_balance()



# class Employee:
#     _base_salaries = {
#         'trainee': 1000,
#         'junior' : 2000,
#         'mid-level' : 3000,
#         'senior' : 4000,
#     }
#     def __init__(self,name, level):
#         if not (isinstance(name, str) and isinstance(level,str)):
#             raise TypeError("'name' and 'level' attribute must be of type 'str'.")
        
#         if level not in Employee._base_salaries:
#             raise ValueError(f"Invalid value '{level}' for 'level' attribute")
#         self._name = name
#         self._level = level
#         self._salaries = Employee._base_salaries[level]
        
#     def __str__(self):
#         return f"{self.name} : {self.level}"
    
#     def __repr__(self):
#         return f"Employee('{self.name}', '{self.level}')"
    

#     @property
#     def name(self):
#         return self._name
    
#     @property
#     def level(self):
#         return self._level
    
    


# charlie_brown = Employee("Charlie Brown", "Trainee")

# print(repr(charlie_brown))













# # # to-do list manager

# # class to_do_list:
# #     todo_list = []

    

# #     def choice(self):
        
# #         while True:
# #             choice = int(input("1: Add Task | 2: View Task | 3: Mark done | 4: Quit: "))
# #             if choice == 4:
# #                 print("Bye")
            
# #             elif choice == 1:
# #                 while True:
# #                     task =input("ENter task (q to quit): ")
# #                     to_do_list.todo_list.append(task)
# #                     if task.lower == "q":
# #                         break
# #                     print("------------- Tasks Added ---------------")




# import time
# class tracker:
#     start_time = None
#     total_time = 0 

#     def __init__(self,choose):
#         self.choose = choose
    
#     def one(self):
#         while True:
            
#             if self.choose == "1":
#                 tracker.start_time =  time.time()
#                 print("Study Started")
#                 continue
                
#             elif self.choose == "2":
#                 if tracker.start_time is None:
#                     print("You haven't started studying")
#                     continue
#                 else:
#                     end_time = time.time()
#                     tracker.total_time += end_time - tracker.start_time
# #                     tracker.start_time = None
# #                     print("Study Stopped")
# #             elif self.choose == "3":
# #                 mins = tracker.total_time / 60
# #                 print(f"Total study time: {mins:.2f} minutes")
            
# #             elif choose == "4":
# #                 break




# # print("1. Start Studying")
# # print("2. Stop Studying")
# # print("3. Show Total time")
# # print("4. Exit")

# # choose = input("Choose: ")
# # user1 = tracker(choose)
# # user1.one()
            






# #PYTHONH  file detection
# import os

# file_path = "test.txt" #relative reference # get the file extension right
# file_path2 = "stuff/test2.txt"
# file_path3 = "C:/Users/DARAMZ/Desktop/test3.txt"
# folder_path = "C:/Users/DARAMZ/Desktop/merlin"
# if os.path.exists(folder_path):
#     print(f"The location '{folder_path}' exists")


#     if os.path.isfile(folder_path):
#         print("That is a file")
#     elif os.path.isdir(folder_path):
#         print(f"'{folder_path}' is a folder/directory")

# else:
#     print("That location doesn't exist")





#python writing files (.txt, .json, .csv)



# "w" - write
#     # "x" - it also write if the "output.txt" doesn't exists
#     # "a" - append; to append a file
#     # "r" - to read


# txt_data = "i like pizza!!"

# file_path = "test.txt"

# file_path3 = "C:/Users/DARAMZ/Desktop/test3.txt"
# with open(file_path, "w") as file:
#     file.write(txt_data)
#     print(f"txt file {file_path} was created")


# print()
# try:
#   with open(file_path3, "x") as file:  #x
#       file.write(txt_data)
#       print(f"txt file {file_path3} was created")

# except FileExistsError:
#    print("That file already exists")

# print()


# with open(file_path, "a") as file:
#     file.write("\n" + txt_data)
#     print(f"txt file {file_path} was created")


# employees = ["Eugene", "Squidward", "Spongebod", "Patrick"]
# try: 
#     with open(file_path3, "w") as file:
#         for employee in employees:
#             file.write(employee + " ")
#         print(f"txt file '{file_path3}' was created")

# # except FileExistsError:
# #     print("That file already exists")



# # # .json is made of up key value pairs


# # import json
# # employee = { 
# #     "name": "Spongebob",
# #     "age": 30,
# #     "job" : "cook"
# # }

# # file_path3 = "C:/Users/DARAMZ/Desktop/test3json.json"

# # try: 
# #     with open(file_path3, "w") as file:
# #         json.dump(employee, file, indent=4)
# #         print(f"json file '{file_path3}' was created")

# # except FileExistsError:
# #     print("That file already exists")





# #.csv


# import csv
# employee = [["Name", "Age", "Job"],
#             ["Spongebob", 30, "cook"],
#             ["patrick", 37, "Unemployed"],
#             ["Sandy", 34,"Scientist"]]
# file_path3 = "C:/Users/DARAMZ/Desktop/test3csv.csv"

# try: 
#     with open(file_path3, "w", newline="") as file:
#         writer = csv.writer(file)
#         for row in employee:
#             writer.writerow(row)
#         print(f"csv file '{file_path3}' was created")

# except FileExistsError:
#     print("That file already exists")



#python reading files

# file_path3 = "C:/Users/DARAMZ/Desktop/test3.txt"
# try:
#     with open(file_path3, "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("That file was not found")



# import json
# file_path3 = "C:/Users/DARAMZ/Desktop/test3.json"
# try:
#     with open(file_path3, "r") as file:
#         content = json.load(file)
#         print(content["job"])
# except FileNotFoundError:
#     print("That file was not found")





# import csv
# file_path3 = "C:/Users/DARAMZ/Desktop/test3csv.csv"
# try:
#     with open(file_path3, "r") as file:
#         content = csv.reader(file)
#         for line in content:
#             print(line[1])
# except FileNotFoundError:
#     print("That file was not found")






# # smart file checker
# import os 
# print("====== Smart file Checker =====")
# filename = input("Enter file name: ")
# if os.path.exists(filename):
#        print("This file exists")

#        with open(filename, "r") as file:
#                content = file.read()
               
            
#        if content.strip()== "":
#                print("This file is empty")

#                write = input("Do you want to write something in the file (y/n): ").lower()
#                if write == "y":
#                       message = input("What do you want to write: ")
#                       with open(filename, "a") as file:
#                              file.write(message)
#                       print("✅ Message saved")
#                else:
#                       print("ALright file still empty")

                             
                             
#        else:
#             print("This file has content")
#             print("------ Preview ------")
#             print(content[:200])

    

# else:
#         print("This file doesn't exists")

#         create = input("Do you want to create it? (y/n): ").lower()
#         if create == "y":
#                with open(filename, "w") as file:
#                       file.write("") # creates an empty file
#                print("File created successfully")
#         else:
#                print("NO file created")



# #date and time

# import datetime
# # date = datetime.date(2026, 2, 18)
# # today =  datetime.date.today()
# # time = datetime.time(12, 30, 00)
# # now = datetime.datetime.now()
# # now = now.strftime("%H:%M:%S %d/%m/%Y")
# # print(today)
# # print(date)
# # print(time)
# # print(now)




# target_datetime = datetime.datetime(2032, 1, 2, 12, 30, 1)
# current_datetime = datetime.datetime.now()

# if target_datetime < current_datetime:
#     print("Target date has passed")

# else: 
#     print("Target date has not passed")



# #alarm clock

# import time
# import datetime
# import pygame

# def set_alarm(alarm_time):
#     print(f"Alarm set for {alarm_time}")
#     sound_file = "My_music.mp3"
#     is_running =  True

#     while is_running:
#         current_time = datetime.datetime.now().strftime("%H:%M:%S")
#         print(current_time)

#         is_running = False


# if __name__ == "__main___":
#     alarm_time = input("Enter the alarm time (HH:MM:SS): ")
#     set_alarm(alarm_time)




# import datetime

# Filename = "note.txt"
# def add_note():
#     note  = input("Write your notes: ")
#     time_now = datetime.datetime.now().strftime("%d/%m/%Y  %H:%M:%S")

#     with open(Filename, "a") as file:
#         file.write(f"[{time_now}]  {note} \n")
    
#     print("✅ Note saved")


# # def view_note():
# #     try: 
# #         with open(Filename, "r") as file:
# #             content = file.read()
# #         if content.strip() == "":
# #             print("⚠ no notes yet!!")
# #         else:
# #             print("=== Your Notes ====")
# #             print(content)
# #     except FileNotFoundError:
# #         print("NO note file found yet")

# # def clear_note():
# # #    with open(Filename, "w") as file:
# # #        file.write("")
# # #        print("Notes cleared")  to clear notes OR
# #     open(Filename, "w").close()
# #     print("Notes cleared")


# # while True:
# #     print("==== Notes Saver App ====")
# #     print("1. Add note")
# #     print("2. View notes")
# #     print("3. Clear notes")
# #     print("4. Exit")

# #     choice = input("Choose an option: ")

# #     if choice == "1":
# #         add_note()
    
# #     elif choice == "2":
# #         view_note()
    
# #     elif choice == "3":
# #         clear_note()
    
# #     elif choice == "4":
# #         print("Goodbye")
# #         break
    
# #     else: 
# #         print("Invalid choice")




# # import os 
# # import datetime

# # FILENAME = "mynotes.txt"
# # def ensure_file():
# #     if not os.path.exists(FILENAME):
# #         open(FILENAME, "w").close()
# #         print("Notes file created ")
# #     else: 
# #         print("Note not found")


# # def add_notes():
# #     note = input("Enter your note: ")
# #     time_stamp = datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
# #     with open(FILENAME, "a") as file:
# #         content = file.write(f"[{time_stamp}]  {note} \n")
# #         print("Note added")
    

# # def view_notes():
    
# #         with open(FILENAME, "r") as file:
# #             read = file.read()
# #             if read.strip() == "":
# #                  print("No note yet")
# #             else:
# #                  print("===== Notes =====")
# #                  print(f"{read} \n ")


# # def file_status():
# #      size = os.path.getsize(filename= FILENAME)
# #      if size == 0 :
# #           print("This file is empty")
# #      else:
# #           print(f"The File size is '{size}' ")

# # ensure_file()

# # while True:
# #      print("====== Menu ======")
# #      print("1. Add notes")
# #      print("2. View notes")
# #      print("3. File Status")
# #      print("4. Exit")

# #      choice  = input("Choose an option: ")

# #      if choice == "1":
# #           add_notes()
# #      elif choice ==  "2":
# #           view_notes()
# #      elif choice == "3":
# #           file_status()
# #      elif choice == "4":
# #           print("Goodbye!!!")
# #           break
# #      else:
# #           print("Invalid option")
        





# # # User profile saver
# # # a program that saves a user profile(name , age, fav subject) into a json file
# # import json
# # import os

# # def create_file(filename):
# #     if os.path.exists(filename):
# #           print("****** File already exist *****")
          
               
    
# #     else:
# #          print("=== Creating new file..=====")
# #          with open(filename, "w") as file:
# #                file.write("")
# #                print("FIle created successfully")


# # def add_profile():
# #      name = input("Enter your name: ")
# #      age = input("Enter your age: ")
# #      fav_subject = input("Enter your fav subject: ")

# #      profile = {
# #           "name": name,
# #           "age" : age,
# #           "Favorite subject" : fav_subject
# #      }
# #      with open(filename, "w") as file:
# #           json.dump(profile, file, indent=4)
     
# #      print("***** Profile saved *****")

# # def view_profile():
# #      with open(filename, "r") as file:
# #           content = json.load(file)
# #           if content:
# #                print("===== User Profile =====")
# #                for key, value in content.items():
# #                     print(f"{key.capitalize()} : {value}")
# #                     print("====================")
# #                print()
# #           else: 
# #                print("NO profile found")





# # while True:
# #      print("===== JSON Profile Saver =====")
# #      print("1. Create file")
# #      print("2. Add profile")
# #      print("3. View profile")
# #      print("4. Exit")

# #      choice = input("Enter a choice: ")

# #      if choice == "1":
# #           filename = input("Enter a file name to create a .json file (add .json at the end of the name): ").lower()
# #           create_file(filename)
# #      elif choice == "2":
# #           add_profile()
# #      elif choice == "3":
# #           view_profile()
# #      elif choice == "4":
# #           print("Goodbye")
# #           break
# #      else:
# #           print("Invlaid choice")




# # Study Traker
# import os
# import json
# import datetime
# Filename = "Study_planner.json"

# def ensure():
#     if os.path.exists(Filename):
#         print("Study tracker created")

# def add_session():
#     subject = input("Enter subject: ")
#     start_time = input("Enter Start time(HH:MM): ")
#     stop_time  = input("Enter Stop time(HH:MM): ")

#     session = {
#         "Subject" : subject,
#         "Start Time" : start_time,
#         "Stop Time" : stop_time
#     }

#     with open(Filename, "a") as file:
#         file.write(json.dumps(session))


# add_session()
# # def view_summary():
# #     with open(Filename, "r") as file:
# #         content = json.load(file)
     
# #     if not content:
# #         print("No study seesions")
# #         return
# #     totals = {}
# #     print("======== All Sessions ======")
# #     for session in content:
# #         print(f"{session['subject']} : {session['hours']} hours")
#         totals[session['subject']]
     
        















# # #TXT File MODE
# # #"W"- overwrite or create     #file.write

# # with open("Example.txt", "w") as file:
# #     file.write("Hello world")

# # # create file if missing
# # # deletes old content if file exists



# # #"R"- read entire file   #file.read()
 
# # with open("Example.txt", "r") as file:
# #     content = file.read()
# #     print(content)


# # # "A" -  add to end- keeps old content

# # with open("Example.txt", "a") as file:   #file.write()
# #     file.write("Addded later")



# # # JSON FILE MODES
# # # always import json

# # # "W" - overwrites file with new json  # json.dump()

# # data = {
# #     "name" : "dara",
# #     "age"  : 22
# # }

# # with open("Example.json", "w") as file:
# #     json.dump(data, file, indent=4)


# # "R" 
# with open("example.json", "r") as file:
#     content = json.load(file)
#     print(content["name"])



# # # # "A" - for this you have to read - modify- write back
# # import json
# # new_item ={"name" : "daa",
# #     "age"  : 25}

# # with open("data.json", "a") as file:
# #     file.write(json.dumps(new_item))



# # "W"
# import csv

# with open("Scores.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerrow([])



# #"R"
# import csv
# with open("scores.csv", "r") as file:
#     reader = csv.reader(file)

#     for row in reader:
#         print(row)


# #"A"

# import csv
# with open("scores.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow("dara", 64)








# # Csv project 
# # Student Score logger

# import os
# import csv
# fileName = "score_logger.csv"
# def header():
#     with open(fileName, "w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow(["name", "score"])

# def add_score():
#     name = input("Enter name: ")
#     score = input("Enter score: ")

#     with open(fileName, "a") as file:
#         writer = csv.writer(file)
#         writer.writerow([name, score])

#     print("Score added")

# def view_score():
#     with open(fileName, "r") as file:
#         reader = csv.reader(file)
#         rows = list(reader)
        
#     if len(rows) <= 1:
#         print("No scores yet \n")
#         return
#     print("====== All Scores =====")
#     for row in rows:
# #         print(", ".join(row))
# #     print()
# # view_score()

# import os
# import csv
# filenaMe = "Expense_traker.csv"

# with open(filenaMe, "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["item ", " amount ", " category"])


# def add_expenses():
#     item = input("Item name: ")
#     amount  = float(input("Enter amount: "))
#     category = input("Category: ")

#     with open(filenaMe, "a",  ) as file:
#         writer = csv.writer(file)
#         writer.writerow([item, amount, category])


# def view_expenses():
#     with open(filenaMe, "r") as file:
#         reader = csv.reader(file)
#         rows = list(reader)
#         if len(rows) <1: 
#             print("No expenses yet")
#             return
        
#         total = 0 
#         print("===== Expenses ====")
#         for row in rows[1:]:
#             if len(row) >=3:
#                 print(f"{row[0]} | {row[1]} | {row[2]}")
#                 total += float(row[1])
        
#         print(f"Total spent: {total}")

# while True:
#      print("===== CSV EXPENSE TRACKER =====")
     
#      print("1. Add Expenses")
#      print("2. View summary")
#      print("3. Exit")

#      choice = input("Enter a choice: ")

#      if choice == "1":
          
#           add_expenses()
#      elif choice == "2":
#           view_expenses()
          
#      elif choice == "3":
#           print("Goodbye")
#           break
#      else:
#           print("Invlaid choice")








# from datetime import datetime
# import os
# import csv
# filenamE = "C:/Users/DARAMZ/Desktop/Study_planner.csv"

# def add_tracker():
#     subject = input("Enter Subject: ")
#     start_input = input("Start time(HH:MM): ")
#     stop_input = input("Stop time(HH:MM): ")


#     file_exits = os.path.isfile(filenamE)

#     with open(filenamE, "a", newline="") as file:
#             writer = csv.writer(file)

#             if not file_exits:
#                  writer.writerow(["SUBJECT", "START TIME", "STOP TIME", "TOTAL TIME"])
        

    
   
    
#     start_time = datetime.strptime(start_input, "%H:%M")
#     stop_time = datetime.strptime(stop_input, "%H:%M")

#     time_diff = stop_time - start_time
#     total_seconds = int(time_diff.total_seconds())
#     hours = total_seconds // 3600           # // - floor divison : removes demicals
#     minutes = (total_seconds % 3600) // 60
#     total_time = f"{hours}:{minutes}"

#     with open(filenamE, "a") as file:
#         writer = csv.writer(file)
#         writer.writerow([subject, start_input, stop_input, total_time])

# def view_tracker():
#     with open(filenamE, "r") as file:
#         reader = csv.reader(file)
        
#         for row in reader:
#             print(row)






# while True:
#      print("===== CSV STUDY TRACKER =====")
     
#      print("1. Add Tracker")
#      print("2. View summary")
#      print("3. Exit")

#      choice = input("Enter a choice: ")

#      if choice == "1":
#          add_tracker()
          
          
#      elif choice == "2":
#           view_tracker()
          
#      elif choice == "3":
#           print("Goodbye")
#           break
#      else:
#           print("Invlaid choice")








# congrats to me i have completely catch up to hello.py




# # projects on multit-threading
# import threading
# import time

# def countdown():
#     for i in range(5,0,-1):
#         print(f"Countdown: {i}")
#         time.sleep(1)
#     print("Countdown finished..")

# def Type_message():
#     message = "Multithreading is powerful"

#     for char in message:
#         print(char, end="", flush=True)
#         time.sleep(0.1)
#     print("\n Typing finished")


# t1 = threading.Thread(target=countdown)
# t2 = threading.Thread(target=Type_message)

# t1.start()
# t2.start()

# t1.join()
# # t2.join()

# import threading
# import time
# def logger():
#     while True:
#         print(f"[LOG] program running...")
#         time.sleep(5)

# # daemon thread =stops when the main program exits

# def main_program():
#     while True:
#         user_input = input("Enter something (type 'exit to quit): ")
#         if user_input == "else": 
#             print("Bye")
#             break
#         print(f"You entered: {user_input}")

# logger_thread = threading.Thread(target=logger, daemon=True)
# logger_thread.start()
# main_program()
# print("Program exited")





# # multi file reader
# import threading
# file1 = "file1.txt"
# file2 = "file2.txt"
# file3 = "file3.txt"
# def read_file(filename):
#     try:
#         with open(filename, "r") as file:
#             lines = file.readline()
#             print(f"{filename} has {len(lines)} lines")
#     except FileNotFoundError:
#         print(f"{filename} not found")

# files = [file1, file2, file3]
# threads = []

# for file in files:
#     t1 = threading.Thread(target=read_file, args=(file, ))
#     threads.append(t1)
#     t1.start()

# for t1 in threads:
#     t1.join()

# print("All files processed")

# random joke generator

# import requests

# def get_joke():
#     joke_url = "https://official-joke-api.appspot.com/random_joke"
#     response = requests.get(joke_url)

#     if response.status_code == 200:
#         data = response.json()
#         print("\n Here your joke: \n")
#         print(data["setup"])
#         print(data["punchline"])
    
#     else:
#         print(f"Error: could not get joke")

# while True:
#         get_joke()

#         another_joke = input("DO you want another joke? (y/n): ")

#         if another_joke != "y":
# #             print("Goodbye")
# #             break


# # randon activity generator

# import requests


# def get_request():
#     url = "https://www.boredapi.com/api/activity"

#     response = requests.get(url)

#     if response.status_code == 200:
#        data =  response.json()
#        print("\n Activity Idea: \n")
#        print("Activity name", data["activity"])
#        print("Type", data["type"])
#        print("Participants", data["participants"])
#        print("Price", data["price"])


#     else:
#         print("Error in url")


# while True:
#     get_request()
#     choice =  input("Do you want another activity? (y/n): ").lower()

#     if choice != "y":
#         print("Bye")
#         break


#SMART CONTACT MANAGER


# import json

# filename = "contacts.json"
# def load_contacts():
#     try: 
#         with open(filename, "r") as file:
#             return json.load(file)
#     except (FileNotFoundError, json.JSONDecodeError):
#         return []
    

# def save_contact(contacts):
#     with open(filename, "w") as file:
#         json.dump(contacts, file, indent=4)

# def contact_info(contacts):
#     name = input("Name: ")
#     phone = input("Phone Number: ")
#     email = input("Email: ")

#     contact = {
#         "Name" : name,
#         "Phone Number" : phone,
#         "Email Address" : email
#     }

#     contacts.append(contact)
#     save_contact(contacts)
#     print("Contact added")


# def view_contacts(contacts):
#     if not contacts:
#         print("No contact found")

#     for contact in contacts:
#         print(f"\n Name: {contact['Name']}")
#         print(f"Phone Number: {contact["Phone Number"]}")
#         print(f"Email Address: {contact["Email Address"]}")


# def delete_contact(contacts):
#     name = input("Enter name to delete the contact: ")
#     found = False

#     for c in contacts:
#         if c["Name"].lower() == name.lower():
#             contacts.remove(c)
#             save_contact(contacts)
#             print("Deleted")
#             found = True
#             break
#     if not found:
#         print("Contact not found")

# contacts = load_contacts()
# while True:
#     print("\n1. Add\n2. View\n3. Delete\n4. Exit")
#     choice = input("Choose: ")

#     if choice == "1":
#         contact_info(contacts)
#     elif choice == "2":
#         view_contacts(contacts)
#     elif choice == "3":
#         delete_contact(contacts)
#     elif choice == "4":
#         break
#     else:
#         print("Invalid choice.")







# expense tracker

# import json
# filename = "expenses.json"

# def load_expenses():
#     try:
#         with open(filename, "r") as file:
#             return json.load(file)
    
#     except (FileNotFoundError, json.JSONDecodeError):
#         return []


# def save_expenses(expenses):
#     with open(filename, "w") as file:
#         json.dump(expenses, file, indent=4)

# def add_expenses(expenses):
#     try:
#         amount = float(input("Enter amount: $"))
#     except ValueError:
#         print("Invalid amount. please enter a number.")
#         return
        
    
#     category = input("Category: ")


#     expense = {
#         "Amount" : amount,
#         "Category" : category
#     }

#     expenses.append(expense)
#     save_expenses(expenses)
#     print("Expenses added successfully")

# def view_expenses(expenses):
#  if not expenses:
#     print("You haven't bought anything!!")
#     return
#  for e in expenses:
#         print(f"{e['Category']} - {e['Amount']:.2f}")
    
# def show_total(expenses):
#     total =  sum(e["Amount"] for e in expenses)
    
#     print(f"\n Total Spent: ${total:.2f}")
        
# def category_summary(expenses):
#     if not expenses:
#         print("NO expenses recorded")
#         return
    
#     totals ={}

#     for e in expenses:
#         category = e["Category"]
#         amount = e["Amount"]
        
        
#         if category not in totals:
#             totals[category] = 0

#         totals[category] += amount

#     print("\n--- Category Summary ---")
#     for category, total in totals.items():
#         print(f"{category}: ${total:.2f}")


# expenses = load_expenses()

# while True:
#     print("\n1. Add Expense")
#     print("2. View Expenses")
#     print("3. Show Total Spent")
#     print("4. Category Summary")
#     print("5. Exit")

#     choice = input("Choose an option: ")

#     if choice == "1":
#         add_expenses(expenses)
#     elif choice == "2":
#         view_expenses(expenses)
#     elif choice == "3":
#         show_total(expenses)
#     elif choice == "4":
#         category_summary(expenses)
#     elif choice == "5":
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please try again.")



# #Personal Journal




# import json
# from datetime import datetime

# entries_file = "entries .txt"
# metadata_file = "journal.json"


# def load_metadata():
#     try:
#         with open(metadata_file, "r") as file:
#             return json.load(file)
#     except (FileNotFoundError, json.JSONDecodeError):
#         return{"entries": 0}

# def save_metadata(data):
#     with open(metadata_file, "w") as file:
#         json.dump(data, file, indent=4)

# def add_entry(metadata):
#     entry = input("Write your journal entry: \n")
#     date = datetime.now().strftime("%d-%m-%y    %H:%M:%S")

#     with open(entries_file, "a") as file:
#         file.write(f"\n [{date}] \n{entry}\n")

#         metadata["entries"] += 1
#         save_metadata(metadata)
#         print("Entry saved")

# metadata = load_metadata()



# while True:
#     print("Personal Journal")
#     print("\n 1. Add Entry")
#     print("2. View Number of Entries")
#     print("3. Exit")
  

#     choice = input("Choose an option: ")

#     if choice == "1":
#         add_entry(metadata)
#     elif choice == "2":
#         print(f"Total entries: {metadata['entries']}")
    
#     elif choice == "3":
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid choice. Please try again.")



## PyQt5

# PyQt5 is a library that lets you create desktop applications
#  with windows, buttons, text, images, menus, etc.




# every PyQt app has 3 main parts
# 1. Application object  = QApplication(sys.argv)  this run the program
# 2. Window(QWidget) = window = QWidget             window.show()       what the user sees
# 3. Event Loop = this keeps the app alive  sys.exit(app.exec_())  without this the window closes immediately


# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5.QtWidgets import QLabel
# from PyQt5.QtCore import Qt

# app = QApplication(sys.argv)
# window = QWidget()

# window.setWindowTitle("My First app")
# window.resize(400, 300)  #(width,length) (x, y)
# label = QLabel("BANKAI", window)
# label.move(100, 100)
# label.setGeometry(0,0,400,300)
# label.setStyleSheet("color:blue; font-size: 50px;")
# label.setAlignment(Qt.AlignCenter)

# window.show()



# sys.exit(app.exec_())



# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QIcon


# app = QApplication(sys.argv)
# window = QWidget()

# window.setWindowTitle("Profile Card App")
# window.resize(400, 300)
# window.setWindowIcon(QIcon("aizen.jpg"))
# label = QLabel("Name: Darasimi", window)
# label2 = QLabel("Course: Python Developer", window)
# label3 = QLabel("Level: Beginner", window)

# label.setGeometry(0,40,400,40) # (x,y, width, height)
# # x -> horizontal postion(left -> right)
# # y -> Vertical postion (top -> downn)
# # width -> how wide the label is 
# # height -> how tall the label is
# label2.setGeometry(0,90,400,40)
# label3.setGeometry(0,140,400,40)


# label.setAlignment(Qt.AlignCenter)
# label2.setAlignment(Qt.AlignCenter)
# label3.setAlignment(Qt.AlignCenter)

# label.setStyleSheet("color: red; font-size: 20px;")
# label2.setStyleSheet("color: blue; font-size: 15px;")
# label3.setStyleSheet("color: green; font-size: 10px;")




# window.show()

# sys.exit(app.exec_())





# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setGeometry(500,200, 500,500)
#         self.setWindowTitle("bankai")
      


# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()




# # images
# # images= QLabel +QPixmap    ------->> label.setPixmap(pixmap)



# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel 
# from PyQt5.QtGui import QPixmap


# class Mainwindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setGeometry(500,200,500,500)
#         self.setWindowTitle("Image project")

#         label = QLabel(self)
#         label.setGeometry(0,0, 250,250)
#         pixmap = QPixmap("aizen.jpg")

#         label.setPixmap(pixmap)
#         label.setScaledContents(True)
#         label.setGeometry((self.width() -label.width()) // 2,
#                           (self.height() - label.height())//2,
#                             label.width(),
#                               label.height())
        

        


        



# def main():
#     app = QApplication(sys.argv)
#     window = Mainwindow()
#     window.show()
#     sys.exit(app.exec_())
    


# if __name__ == "__main__":
#     main()

# # 












# # Profile picture Card


# import sys
# from PyQt5.QtWidgets import  QApplication, QMainWindow, QLabel
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtCore import Qt


# class Mainwindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
        
#         self.setWindowTitle("Profile Picture Card")
#         self.setGeometry(500,200,500,500)
#         label = QLabel(self)
#         pixmap = QPixmap("aizen.jpg")
#         label.setPixmap(pixmap)
#         label.setGeometry(150,30, 200,200)
#         label.setScaledContents(True)


#         label2 = QLabel("Name:    ", self)
#         label3 = QLabel("Course:   ", self)
#         label4 = QLabel("Level:    ", self)
#         label2.setGeometry(50,250, 400,50 )
#         label3.setGeometry(50,300, 400,50 )
#         label4.setGeometry(50,350, 400,50 )

#         label2.setAlignment(Qt.AlignCenter)
#         label3.setAlignment(Qt.AlignCenter)
#         label4.setAlignment(Qt.AlignCenter)

#         label2.setStyleSheet("color: red; font-size: 30px; font-weight: bold;")
#         label3.setStyleSheet("color: blue; font-size: 22px; font-weight: bold;")
#         label4.setStyleSheet("color: purple; font-size: 18px; font-weight: bold;")



# def main():
#     app = QApplication(sys.argv)
#     window = Mainwindow()
#     window.show()

#     sys.exit(app.exec_())



# if __name__== "__main__":
#     main()




# Layout Managers
# B4 layout i was using
#setGeometry(x, y, width, height)  --> this is called absolute postioning


# Main Layout Types
# QVBoxLAyout (Vertical)
# QHBoxLayout (Horizontal)
# QGridLayout (Grid / Table)
# Nested Layout

# Grid
# [0,0]  [0,1]
# [1,0]  [1,1]




# Basic LAyout Pattern

# layout = QVBoxLayout()

# layout.addWidget(widget)

# container = QWidget()
# container.setLayout(layout)

# self.setCentralWidget(container)






# import sys
# from PyQt5.QtWidgets import ( QApplication, QLabel, QMainWindow, QWidget,
#                               QVBoxLayout)
# from PyQt5.QtGui import QPixmap
# from PyQt5.QtCore import Qt
# class Mainwindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
        
#         self.resize(400, 500)
#         self.initUI()


#     def initUI(self):
#         central = QWidget()
#         self.setCentralWidget(central)

#         layout = QVBoxLayout()
        
#         central.setLayout(layout)
#         label = QLabel(self)
#         pixmap = QPixmap("aizen.jpg")

#         label.setPixmap(pixmap)
#         label.setPixmap(pixmap.scaled(200, 200, Qt.KeepAspectRatio))

#         label.setAlignment(Qt.AlignCenter)

#         label2 = QLabel("Name: DARAMZ")
#         label3 =  QLabel("Course: Python DEV")
#         label4 = QLabel("Level: Beginner")

#         label2.setAlignment(Qt.AlignCenter)
#         label3.setAlignment(Qt.AlignCenter)
#         label4.setAlignment(Qt.AlignCenter)

#         label2.setStyleSheet("color: red;")
#         label3.setStyleSheet("color: purple;")
#         label4.setStyleSheet("color: blue;")

#         layout.addWidget(label)
#         layout.addWidget(label2)
#         layout.addWidget(label3)
#         layout.addWidget(label4)

        





# def main():
#     app = QApplication(sys.argv)
#     window = Mainwindow()
#     window.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()



# #PyQt5 buttons

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
# from PyQt5.QtCore import Qt

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Button Example")
#         self.setGeometry(500,200,500,500)

#         self.label = QLabel("Hello", self)
#         self.label.setGeometry(0,50,400,40)
#         self.label.setAlignment(Qt.AlignCenter)

#         self.button =QPushButton("Click Me", self)
#         self.button.setGeometry(150,150,100,40)
#         self.button.setCheckable(True)
#         self.button.clicked.connect(self.button_clicked)
#        # self.button.clicked.connect(self.change_text)
        
#    # def change_text(self):
#        # self.label.setText("Button Clicked!!")
#     def button_clicked(self, checked):
#         if checked:
#             self.label.setText("Button is on")
#             self.button.setText("Turn off")
#         else:
#             self.label.setText("Hello")
#             self.button.setText("click me")

        

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()





# # Click Counter App
# # Button -> Increases number each click
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(500,200,500,500)
#         self.setWindowTitle("Click Counter APP")
#         self.count = 0
#         self.label = QLabel("Count: 0", self)
#         self.label.setGeometry(0,50,500,50)

#         self.button = QPushButton("Click", self)
#         self.button.clicked.connect(self.increase_count)

    
#     def increase_count(self):
#         self.count += 1
#         self.label.setText(f"Count: {self.count}")
        
        


        


# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()






# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(500,200,500,500)
#         self.button = QPushButton("Click me",self)
       
#         self.label = QLabel("Bankai",self)
       
#         self.label.setGeometry(0,20,500,60)
#         self.button.setCheckable(True)

#         self.button.clicked.connect(self.changed)
        

#         self.button.clicked.connect(self.change)

    
#     def changed(self):

#         self.label.setText("Zankai no Tachi")
#         self.button.setText("Bankai")
    
#     def change(self,checked): 
#         if checked:
#             self.label.setText("Tenza zangstu")
    
         

        
        


# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()






# # Dark Mode Toggle App

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox, QVBoxLayout, QWidget
# from PyQt5.QtCore import Qt

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(500,200,500,500)
#         self.setWindowTitle("Dark Mode Toggle App")
#         self.initUi()


#     def initUi(self):
#         self.label = QLabel("Dark Mode: OFF", self)
#         self.label.setAlignment(Qt.AlignCenter)  
        
#         self.central = QWidget()
#         self.setCentralWidget(self.central)
#         layout = QVBoxLayout()
#         self.central.setLayout(layout)

#         layout.addWidget(self.label)

        

#         self.label.setStyleSheet("font-size: 30px;")
#         self.checkbox = QCheckBox("Enable Dark Mode", self)
        
#         layout.addWidget(self.checkbox)
        
#         self.checkbox.setStyleSheet("font-size: 40px;")
#         self.checkbox.setChecked(False)
#         self.checkbox.stateChanged.connect(self.toggle_dark_mode)
    
#     def toggle_dark_mode(self,state):
#         if state == Qt.Checked:
#             self.label.setText("Dark Mode: ON")
            
#             self.setStyleSheet("background-color: black;" \
#                                  "color: white;" )
            
            
            
#         else:
#             self.label.setText("Dark Mode: OFF")
#             self.setStyleSheet("")
    


# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
    
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()







# Radio Buttons
# allow user to choose ONE Option from Multiple chocies




# # # Theme Selector App

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget, QLabel,QVBoxLayout, QRadioButton
# from PyQt5.QtCore import Qt
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(500,200,500,500)
#         self.setWindowTitle("Theme Selector App")
#         self.initUi()
    
#     def initUi(self):
#         self.central_widget = QWidget()
#         self.setCentralWidget(self.central_widget)

#         layout = QVBoxLayout()
#         self.central_widget.setLayout(layout)

#         self.label = QLabel("Selected Theme: Light")
#         self.label.setAlignment(Qt.AlignCenter) 
#         self.label.setStyleSheet("font-size: 40px")
#         layout.addWidget(self.label)


#         self.radio1 = QRadioButton("Light")
#         self.radio2 = QRadioButton("Dark")
#         self.radio3 = QRadioButton("Blue")
        
#         self.radio1.setStyleSheet("font-size: 25px")
#         self.radio2.setStyleSheet("font-size: 25px")
#         self.radio3.setStyleSheet("font-size: 25px")

#         layout.addWidget(self.radio1)
#         layout.addWidget(self.radio2)
#         layout.addWidget(self.radio3)
        


#         self.radio1.setCheckable(True)
      

#         self.radio1.toggled.connect(self.radio_changed)
#         self.radio2.toggled.connect(self.radio_changed)
#         self.radio3.toggled.connect(self.radio_changed)

        

    

#     def radio_changed(self):
#         radio_button = self.sender()

#         if not radio_button.isChecked():
#             return
        
#         if radio_button == self.radio1:
#             self.setStyleSheet("")
#             self.label.setText("Selected Theme: Light")
            
#         elif radio_button == self.radio2:
#             self.setStyleSheet("background-color: black; color: white")
#             self.label.setText("Selected Theme: Dark")
            
#         elif radio_button == self.radio3:
#             self.setStyleSheet("background-color: blue; color: white")
#             self.label.setText("Selected Theme: Blue")
            





        
        
        

        
        


# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()




# # creating a second WIndow

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel,QVBoxLayout,QPushButton, QWidget

# class SecondWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Second Window")

#         layout = QVBoxLayout()
#         layout.addWidget(QLabel("Welcome to the second window"))
#         self.setLayout(layout)

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(500,200,500,500)
#         layout = QVBoxLayout()
#         self.btn1 = QPushButton("OPEN WINDOW",self)
#         self.btn1.clicked.connect(self.open_Win)
        
        

#         layout.addWidget(self.btn1)
#         self.setLayout(layout)
        
    
#     def open_Win(self):
#         self.second = SecondWindow()
#         self.second.show()
        




# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()





# # Profile From App
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QLineEdit, QTextEdit, QPushButton
# from PyQt5.QtCore import Qt
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(500,200,500,500)
#         self.setWindowTitle("Profile From App")
#         self.initUi()
    
#     def initUi(self):
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)
#         layout = QVBoxLayout()
#         central_widget.setLayout(layout)

#         self.name = QLineEdit()
#         self.name.setPlaceholderText("Enter your name")
#         self.email = QLineEdit()
#         self.email.setPlaceholderText("Enter your email")
#         self.bio = QTextEdit()
#         self.bio.setPlaceholderText("Tell us about yourself")
#         self.submit = QPushButton("Submit",self)
#         self.submit.clicked.connect(self.submit_form)
        

#         self.output_label = QLabel("Profile will appear here")
#         self.output_label.setAlignment(Qt.AlignCenter)
#         self.output_label.setWordWrap(True)
        

#         layout.addWidget(self.name)
#         layout.addWidget(self.email)
#         layout.addWidget(self.bio)
#         layout.addWidget(self.submit)
#         layout.addWidget(self.output_label)

    
#     def submit_form(self):
#         name = self.name.text()
#         email = self.email.text()
#         bio = self.bio.toPlainText()
#         output_text = (
#             f"Name: {name}\n"
#             f"Email: {email}\n"
#             f"Bio: {bio}\n"
#         )
#         self.output_label.setText(output_text)
        



        
        
        

        


# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()







# #PyQt5 Line Edits

# import sys
# from PyQt5.QtWidgets import QApplication,QWidget, QVBoxLayout,QMainWindow, QLabel, QLineEdit, QPushButton

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(500,200,400,250)
#         self.setWindowTitle("Greeting App")
#         self.InitUi()

    
#     def InitUi(self):
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)
#         Vbox = QVBoxLayout()
        
#         label = QLabel("Enter Your Name: ", self)
#         self.name = QLineEdit()
#         self.name.setPlaceholderText("Type Your name")
#         label.setStyleSheet("font-size: 25px; font-family: Arial; font-weight: bold;")
#         self.name.setStyleSheet("font-size: 15px; font-family: Arial; ")



#         age = QLabel("Enter your age: ", self)
#         self.age = QLineEdit()
#         self.age.setPlaceholderText("Type Your age")
#         age.setStyleSheet("font-size: 25px; font-family: Arial; font-weight: bold;")

#         self.age.setStyleSheet("font-size: 15px; font-family: Arial; weight;")


#         self.button = QPushButton("Greet Me",self)
#         self.button.clicked.connect(self.greet_user)
#         self.button.setStyleSheet("font-size: 20px; font-family: Arial; font-weight: bold;")


#         self.output_label = QLabel("Your Greeting will appear here")
#         self.output_label.setStyleSheet("font-size: 18px; font-family: Arial; font-weight: bold;")

#         Vbox.addWidget(label)
#         Vbox.addWidget(self.name)
#         Vbox.addWidget(age)
#         Vbox.addWidget(self.age)
#         Vbox.addWidget(self.button)
#         Vbox.addWidget(self.output_label)


#         central_widget.setLayout(Vbox)
        

#     def greet_user(self):
#         name = self.name.text()
#         age = self.age.text()

#         if not name or not age:
#             self.output_label.setText("Please Enter both name and age")
#             return
        
#         self.output_label.setText(f"Hello {name}, you are {age} years old!")



        


# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()




#STopWatch + Digital Clock App

import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import QTime, QTimer, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,300,600,500)
        self.setWindowTitle("Stopwatch + Digital Clock App")
        
        self.clock_label = QLabel(self)
        self.stop_watch = QLabel("00:00:00",self)
        self.elapsed_time = QTime(0,0,0)

        self.start_button = QPushButton("Start",self)
        self.stop_button = QPushButton("Stop",self)
        self.reset_button = QPushButton("Reset", self)


        self.clock_timer = QTimer(self)
        self.stopwatch_timer = QTimer(self)

        self.initUI()

    
    def initUI(self):
        central_widgit =  QWidget()
        self.setCentralWidget(central_widgit)
        vbox = QVBoxLayout()
        central_widgit.setLayout(vbox)

        vbox.addWidget(self.clock_label)
        vbox.addWidget(self.stop_watch)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.stop_button)
        vbox.addWidget(self.reset_button)

        self.clock_label.setAlignment(Qt.AlignCenter)
        self.stop_watch.setAlignment(Qt.AlignCenter)


        self.start_button.setObjectName("start_button")
        self.stop_button.setObjectName("stop_button")
        self.reset_button.setObjectName("reset_button")
        self.clock_label.setObjectName("clock_label")
        self.stop_watch.setObjectName("stop_watch")

        
        font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        font_id2 = QFontDatabase.addApplicationFont("DS-DIGII.TTF")

        
        font_family1 = QFontDatabase.applicationFontFamilies(font_id)[0]
        font_family2 = QFontDatabase.applicationFontFamilies(font_id2)[0]
         

        my_font1 = QFont(font_family1, 130)
        my_font2 = QFont(font_family2, 110)

        self.clock_label.setFont(my_font1)
        self.stop_watch.setFont(my_font2)

        
        

        self.setStyleSheet(
            """
            QLabel#clock_label{
            color: green;

            }
            QLabel#stop_watch{
            color: blue;

            }
            QLabel{
            
            font-weight: bold;
            
            }

            QPushButton{
            font-size: 50px;
            font-family: Arial;
            
            }
            QPushButton:hover{
            background-color: lightblue;
            color: white;
            }


           
            """
        )
        

        self.start_button.clicked.connect(self.start_stopwatch)
        self.stop_button.clicked.connect(self.stop_stopwatch)
        self.reset_button.clicked.connect(self.reset_stopwatch)
        self.clock_timer.timeout.connect(self.update_clock)
        self.clock_timer.start(1000)
        self.stopwatch_timer.timeout.connect(self.stopwatch_update)
        


        self.update_clock()

    

    def start_stopwatch(self):
        self.stopwatch_timer.start(1000)

    def stop_stopwatch(self):
        self.stopwatch_timer.stop()

    def reset_stopwatch(self):
        self.stopwatch_timer.stop()
        self.elapsed_time = QTime(0,0,0)
        self.stop_watch.setText(self.format_time(self.elapsed_time))
    



        

    def update_clock(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.clock_label.setText(current_time)
    

    def format_time(self,time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def stopwatch_update(self):
        self.elapsed_time = self.elapsed_time.addSecs(1)
        self.stop_watch.setText(self.format_time(self.elapsed_time))

        
def main():
    app = QApplication(sys.argv)
    window = MainWin()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()