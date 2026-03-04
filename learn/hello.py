#VARIABLES
# dolamu="boy"
# print("dami is " + dolamu)
# print(type(dolamu))

#pineapple=11
#print(pineapple)

# first_name="monkey"
# last_name="banana"
# full_name= first_name +" "+ last_name
# print(full_name)

#age=500
#hi=1000
#go=hi-age
#him= "dami has a big ass"
#print(str(go) + " "+ him)


#height=45.4
#print(height)
#print(type(height))


#food="pizza"
#print(f"dami is a {food}")

# dola_is_a_boy=True
# if dola_is_a_boy:
#    print("yes")

# else: 
#    print("no")

#TYPECASTING
# gpa=5.7
# age=44

# gpa = int(gpa)
# print(gpa)


# age = float(age)
# print(age)




# hi=input("are you a boy?: ")
# print(f"his dola boy {hi}")


#arithmetic & math

# friends = 10
# friends = friends + 1
# friends += 1
#friends -= 2

#friends = friends * 3
#friends *= 5

#friends = friends/3
#friends /= 5

#friends = friends ** 2
#friends **= 3
# friends %= 3
#friends = friends % 3

# print(friends)


# x = 3.13
# y = -5
# z = 4

# result = round(x)
# # result = abs(y)
# result = pow(2,2)
#result = max(x,y,z)
#result = min(x,y,z)
# print(result)
#pow = 2^2
#round : rounds up a number
#abs turns negative into postive

# import math

# # print(math.pi)
# # # result = math.sqrt(4)
# result = math.ceil(5.7)
# result = math.floor(8.9)
# print(result)

#math.sqrt = square root

#if-else statement
#age = int(input("enter your age: "))
#if age >=100:
#    print("omo you be legend")
#elif age >= 18 :
#    print("welcome")
##    print("them neva born you")

#else:
 #   print("get out of here")



#response = input("ARE YOU A BOY: yes or no: ")
#if response == "yes":
  #  print("yay")
    
#else: print("eww")

#name = input("enter ur name ")
#if name == "":
 #   print("wetin sup u neva write your name")
#else:
 #   print(f"YOKOSO {name}")


#logical operator
# statement
#temp = 45
#is_raining = False

#if temp > 35 or temp < 0 or is_raining: 
 #   print("yhh")
#else:
#    print("na")
#here at least one statement is true that y it will print yhhh


#and
#temp = 100
#is_sunny = True

#if temp >= 28 and is_sunny:
 #   print("IT HOT OUTSIDE")
  #  print("it sunny")
#else:
  #  print("sad")
    #here it only prints only when both statements are true


#conditional expression
# x if condition else y
#num = 7
#print("positive"if num > 4 else"lower")

#result = "even" if num %2 == 0 else "odd"
#print(result)


#a = 5
#b =6
#max_num = a if a > b else b
#min_num = b if b<a else a
#print(min_num)

#user_role= "admin"
#access_level = "Full access" if user_role == "admin" else "limited access"
#print(access_level)

#strings
# name = input("enter your fullname: ")
# result = len(name)
# result = name.find("e")
# #shows ur the postion of the particular character - .find
# result = name.rfind("d")
# result = name.capitalize()
# result = name.upper()
# #result = name.lower()
# result = name.isdigit()
#result = name.isalpha()
#result = name.isalnum()
# # 
# phone_number = input("enter ur phone number:  ")
# result = phone_number.count("-")
# result = phone_number.replace("-", (" "))
# print(result)
# print(help(str))  

#len - length
#r.find = shows the index of that paricular character


#indexing
#credit_number= "123-34567-8910"
#print(credit_number[0])
#print(credit_number[0:])
#print(credit_number[-1])
#print(credit_number[::3])
#last_digits= credit_number[-4:]
#print(f"XXX-XXXXX-{last_digits}")
#print(credit_number[::-1])



#FORMAT SPECIFIERS
#price1 = 300000.14159
#price2 = -983000.45
#price3 = 120000.34
#for decimal points
#print(f"Price 1 is {price1:.2f}")
#print(f"Price 2 is {price2:.2f}")
#print(f"Price 3 is {price3:.2f}")


#for space
#print(f"Price 1 is {price1:10}")
#print(f"Price 2 is {price2:10}")
#print(f"Price 3 is {price3:10}")
#print(f"Price 1 is {price1:019}")
#print(f"Price 2 is {price2:010}")
#print(f"Price 3 is {price3:010}")

#for left justification
#print(f"Price 1 is {price1:<10}")
#print(f"Price 2 is {price2:<10}")
#print(f"Price 3 is {price3:<10}")


#for right justification
#print(f"Price 1 is {price1:>10}")
#print(f"Price 2 is {price2:>10}")
#print(f"Price 3 is {price3:>10}")


#for center justification
#print(f"Price 1 is {price1:^10}")
#print(f"Price 2 is {price2:^10}")
#print(f"Price 3 is {price3:^10}")

#to indiciate plus(+)sign
#print(f"Price 1 is {price1:+}")
#print(f"Price 2 is {price2:+}")
#print(f"Price 3 is {price3:+}")


# a thousand separator
#print(f"Price 1 is {price1:,}")
#print(f"Price 2 is {price2:,}")
#print(f"Price 3 is {price3:,}")



# while loop
# name = input("ENTER YOUR NAME: ")

# while name == "":
#    print("u did noy enter ur name")
#    name = input("ENTER YOUR NAME: ")
# print(name)

#age = int(input("ENTER YOUR AGE: "))

#while age < 0  :
 #   print("NAME CANT BE NEGATIVE")
  #  age = int(input("ENTER YOUR AGE: "))
    
#print(f"you are age {age} years old")


#food = input("enter the food you like (type q to quit): ")

#while not food == "q":
 #   print(f"yoy like{food} ")
  #  food = input("enter another food you like (type q to quit): ")

#print("bye")

#num = int(input("enter a number btw 1-10 "))

#while num < 1 or num > 10:
 #   print(f"{num} is invalid ")
  #  num = int(input("enter a number btw 1-10 "))

#print(f"your number is {num}")    





# FOR LOOPS
# count down from 1-10
# for x in range(1,11):
#    print(x)

#count down backwards
#for x in reversed(range(1,11)):
 #   print(x)
#print("happy new year")

#count by 2's
#for x in range(1,11,2):
 #   print(x)


# credit_card = "1234-5678-9012-3456"
# for x in credit_card:
#    print(x)
  
# for x in range(1, 21):

#    if x == 13:
#        continue   #continue is used to skip
#    else:
#        print(x)

# for x in range(1, 21):
   
#    if x == 13:
#        break
#    else:
#        print(x)




#nested loop
# for x in range(3):
#   for y in range(1,11):
#     print(y, end=" ")
#   print()  



# rows = int(input("enter the # of rows: "))
# column = int(input("enter the # of column: "))
# symbol = input("enter a symbol to use: ")

# for x in range(rows):
#   for y in range(column):
#     print(symbol, end="")
#   print()  


#collections
#list = []
#set = {}
#tuple = ()

#list
# fruits = ["apple", "banana", "cherry", "orange"]
# print(fruits)
# print(fruits[0])
# print(fruits[1])
# print(fruits[0:2])
# print(fruits[::-1])

# for fruit in fruits:
#     print(fruit)

# print("banana" in fruits)

#list are changebale
# fruits[0] = "kiwi"
# fruits[3] = "grape"
# print(fruits)
# for fruit in fruits:
#     print(fruit)

#fruits.append("mango")

# fruits.remove("apple")
# fruits.insert(2, "pineapple")
# fruits.sort()

# fruits.reverse()
# fruits.clear()
# print(fruits.index("orange"))


# print(fruits.count("banana"))
# print(fruits)



#set
# fruits = {"apple", "banana", "cherry", "orange"}

# # # print("banana" in fruits)
# # # print(len(fruits))
# # # fruits.add("mango")
# # # fruits.remove("banana")
# # fruits.clear()
# # fruits.pop()



# print(fruits)




#tuple
# fruits = ("apple", "banana", "cherry", "orange")
# print("banana" in fruits)
# print(len(fruits))




# print(fruits)



#2d list/collections
# fruits =      ["apple", "banana", "watermelon", "watermelon"]
# vegetables =      ["okra", "cabbage", "spinach", "carrot"]
# meat =        ["chicken", "beef", "turkey", "fish"]

# groceries = [fruits, vegetables, meat]
# print(groceries[2])
# print(groceries[0][1])
# # 0 -rows 1- column = 0 row with 1 column

# for x in groceries:
    
#     for y in x:
#         print(y, end=" ")
#     print()



# #note: \n line break (means new paragraph)

# print("\n mom \n hi")




# #dictionary 
# capitals = {
#     "USA": "Wishingtn D.C",
#     "Nigeria": "Abuja",
#     "India": "New Delhi",
#     "China": "Beijing",
#     "Russia": "Moscow",

# }
# # print(dir(capitals))
# # print(help(capitals))
# # print(capitals.get("China"))

# # print(capitals.get("Japan"))
# #when python doesnt find a key it returns none

# # if capitals.get("Japan"):
# #     print("the country exists")
# # else:
# #     print("the country does not exist")

# # if capitals.get("India"):
# #     print("the country exists")
# # else:
# #     print("the country does not exist")
# # that how to check if a key exists in a dictionary


# # capitals.update({"Germany": "Berlin"})
# # capitals.update({"USA":"Detroit" })
# # updates a dic

# # capitals.pop("China")
# # #remove a key value pair
# # capitals.popitem()
# #removes the last key value pair
# # print(capitals)


# # keys = capitals.keys()

# # print(keys)

# # for key in capitals.keys():
# #     print(key)
# # #returns all the keys in the dictionary
# # values = capitals.values()
# # print(values)

# # for value in capitals.values():
# #     print(value)
# #returns all the values in the dictionary

# items = capitals.items()
# print(items)
# # returns all the key value pairs in the dictionary which resembles a 2d list of tuples
# for key, value in capitals.items():
#  print(f"{key} : {value}")


#random
# import random

# # print(help(random))
# # number = random.randint(1,20)
# # print(number)

# # low = 1
# # high = 100
# # number = random.randint(low,high)
# # number = random.random() # returns a random floating number
# # print(number)

# # options = ("rock", "paper", "scissors")
# # game = random.choice(options)
# # print(game)

# cards = ["2", "3","4","5","6","7","8","9","10","J","Q","K","A"]
# random.shuffle(cards)
# print(cards)





#function - is a block of reusable code
# place () after the function name to invoke it
# def happy_birthday(name,age):
#   print(f"Happy Birthday to {name}! ")
#   print(f"you are {age} years old")
#   print(f"happy birthday to you!")
#   print()

# happy_birthday("bro",40)
# happy_birthday("dami",59)
# happy_birthday("dola",89)




# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount} is due on {due_date} ")

# display_invoice("dara", 700, "07/5/2025")


#return statement = is used to end a function
#                   and send a result back to the caller


# def add(X,Y):
#     z = X + Y
#     return z
# def subtract(X,Y):
#     z = X - Y
#     return z
# def multiply(X,Y):
#     z = X * Y
#     return z
# def divide(X,Y):
#     z = X / Y
#     return z

# print(add(4,5))
# print(subtract(22,33))
# print(divide(3,6))
# print(multiply(5,2))




# def create_name(first, last):
#     first = first.capitalize()
#     # last = last.capitalize()
#     # return first + " " + last
# full_name = create_name("dara","sam")

# print(full_name)



#default arguments = a default value for certain parameters
#                     default is used when that argument is ommited
#                     make your functions mroe flexible, reduces number of arguments
#                     1. postional 2. defaults 3. keyword 4. arbitrary


# def net_price(list_price, discount= 0, tax=0.05):
#     return list_price * (1 - discount) * (1 + tax)


# # print(net_price(500))
# # print(net_price(500,0.1))






##excercise
# import time

# def count(end, start=0,):
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print("done")

# # count(10)
# count(30,15)


#keyword argument = is an argument preceded by a identifier
#                   helps with readability
#                   order of arguments doesn't matter

# def hello(greeting,title,fiirst, last):
#     print(f"{greeting} {title} {fiirst} {last}")

# hello("hello ", title="mr", fiirst="dola", last="pants")

# for x in range(1,11):
#     print(x, end=" ")

# print("1", "2", "3", "4", "5", sep= "-")
# # end and sep are keyword arguent




# def get_phone(country, area, first, last):
#     return f"{country}-{area}-{first}-{last}"

# phone_num = get_phone(country=1, area=123, first=345, last=94943 )

# print(phone_num)






#arbitrary argument 
#      *args = allows you to pass multiple non-key arguments
#     **kwargs = allows you to pass multiple keyword-arguments
#       * unpacking operator
#arg = arugemnts
#kwargs - keyword arguments



# def add(a,b):
#     return a + b

# print(add(1,2,5))
# the function cant be used becuz add() takes 2 positional arguments but 3 were given



# def add(*nums):
#    total = 0
#    for num in nums:
#       total += num
#    return total

# print(add(1,2,3))



# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")

# display_name("Silent", "dara", "Shinobi")


#kwargs
# def print_address(**kwargs):
#     for key in kwargs.keys():
#         print(key)
# print_address(street="123 hhh st",
#               apt="10101" 
#               city="lagos", 
#               state="dd", zip="3443343",)




# def shipping_label(*args, **kwargs):
#     for arg in args:
#         print(arg, end=" ")
#     print()
#     if "apt" in kwargs:
#         print(f"{kwargs.get('street')}{kwargs.get('apt')}")
#     else:
#       print(f"{kwargs.get('city')} {kwargs.get('state')}, {kwargs.get('zip')}")
# shipping_label("dr.", "silent shinobi", "iii",
#                street = "123 fake st.",
#                apt= "100",
#                city="lagos",
#                state = "high",
#                zip = "8888")

#iterables = an object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop

# numbers = [1,2,3,4,5]

# for number in numbers:
#     print(number)
# #list are iterable

# numbers = (1,2,3,4,5)

# for number in numbers:
#     print(number)
# #tuples are iterable


# fruits = {"apple", "orange", "banana", "coconut" }

# for fruit in fruits:
#     print(fruit)
# not although list and tuples can be reversed buh sets cant

# name = "RD Reaper"

# for character in name:
#     print(character, end= " ")


# #dict
# my_dictionary = {
#     "A" : 1,
#     "b" : 2,
#     "c" : 3
# }

# for key in my_dictionary:
#     print(key)
# #for keys 


# for value in my_dictionary.values():
#     print(value)
# #for values


# for key, value in my_dictionary.items():
#     print(f"{key} : {value}")



#membership operators = used to test whether a value or variable is found in a sequence
                        #(string,list,tuple,set or dictionaries)
        #               1. in 2. not in
#in
# word = "apple"

# letter = input("guess a letter in the secret word: ").lower()

# if letter in word:
#     print(f"there is a {letter}")
# else:
#     print(f"{letter} was not found")


# #not in

# word = "apple"

# letter = input("guess a letter in the secret word: ").lower()

# if letter not in word:
#     print(f"{letter} was not found")
# else:
#     print(f"there is a {letter}")



# students = {"dami", "dola", "dara"}

# student = input("enter name of a student: ")

# if student in students:
#     print(f"{student} is a student")
# else:
#     print(f"not a student")


# grades = {
#     "sandy": "a",
#     "dola" : "b",
#     "dami" : "c",

# }
# student = input("enter a name of a student: ")

# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} wasnt found")


# email = input("enter an email: ")

# if "@" in email and "." in email:
#     print("Valid email")
# else:
#     print("Invalid email")




# list comprehension =  a concise way to create lists in python
#              compact and easier to read than traditional loops
          # [EXPRESSION FOR VALUE IN ITERABLE IF CONDITIONS]

#non list comprehension
# doubles = []
# for x in range(1,11):
#     doubles.append(x*2)

# print(doubles)


# #list comprehension

# doubles = [x*2 for x in range(1,10) ]
# print(doubles)



# doubles = [x*2 for x in range(1,11) ]
# triples = [y*3 for y in range(1,11)]
# squares = [z*z for z in range(1,11)]

# print(doubles)
# print(triples)
# print(squares)



# fruits = ["apple", "banana", "orange", "coconut"]
# fruits = [fruit.upper() for fruit in fruits]

# print(fruits)


# fruits = ["apple", "banana", "orange", "coconut"]
# fruit_chars = [fruit[0] for fruit in fruits]
# #for every fruit in fruits return the first character of each string
# print(fruit_chars)


# if condition

# numbers = [1,-2,3,-4,5,-6,8,-7]
# postive_num = [num for num in numbers if num > 0]
# # note if ur not modify the values u can just put the value of num
# negative_num = [num for num in numbers if num < 0]
# even_num = [num for num in numbers if num % 2 == 0]
# odd_num = [num for num in numbers if num % 2 != 0]
# print(postive_num)
# print(negative_num)
# print(even_num)
# print(odd_num)




# grades =[85,42,79,90,56,61,30]
# passing_grades= [grade for grade in grades if grade >= 60]
# print(passing_grades)



#match-case statement (switch); an alternative to using many 'elif' statements
#                       execute some code if a value matches a 'case' 
#                       benefits: cleaner and syntax is more readable

# def days_of_week(day):
    
#     if day == 1:
#         return "it sunday"
#     elif day == 2:
#         return "it monday"
#     elif day == 3:
#         return "it tuesday"
#     elif day == 4:
#         return "it wednesday"
#     elif day == 5:
#         return "it thursday"
#     elif day == 6:
#         return "it friday"
#     elif day == 7:
#         return "it saturaday"
#     else:
#         return "not a valid day"

# print(days_of_week(5))

#match case statement
# def days_of_week(day):
#     match day:
#         case 1:
#               return "it sunday"
#         case 2:
#           return "it monday"
#         case 3:
#           return "it tuesday"
#         case 4:
#           return "it wednesday"
#         case 5:
#           return "it thursday"
#         case 6:
#           return "it friday"
#         case 7:
#           return "it saturaday"
#         case _:
#           return "not a valid day"
# #case _ acts as the else statement
# print(days_of_week(5))




# def is_weekend(day):
#     match day:
#         case "saturday"|"sunday":
#               return True
#         case "monday" |"tuesday"| "wednesday"|"thursday"|"friday" :
#           return False
       
#         case _:
#           return "not a valid day"
# #case _ acts as the else statement
# # | = or 
# print(is_weekend("tuesday"))


# module = a file containing code you want to include in your program
#            use 'import' to include a module(built-in or your own)
#         useful to break up a large program reusable separate files

# print(help("modules"))
# import math

# # to access varaibles and functions in the math module u use math.(name of variable of fuction)
# print(math.pi)


#another way to import

# import math as m
# print(m.pi)

# from math import pi
# print(pi)


# creating a module 
# import example
# reuslt = example.pi
# reuslt = example.square(4)
# reuslt = example.cube(5)
# reuslt = example.circumference(6)
# reuslt = example.area(9)
# print(reuslt)




#variable scope = where a variable is visibe and accessible
#scope resolution = (LEGB) Local -> Enclosed -> Global -> Bult-in
# local 
# def func1():
#     a = 1
#     print(a)


# def func2():
#     b = 2
#     print(b)

# func1()
# func2()




# #enclosed
# def func1():
#     a = 1
    
#     def func2():
#         b = 2
#         print(b)
#     func2()

# func1()


# #global
# def func1():
#     print(x)


# def func2():
   
#     print(x)

# x = 3
# func1()
# func2()



# # Built -in
# from math import e
# def func1():
#   print(e)

# e = 3
# func1()



# if _name_== _main_: (this script can be imported OR run standalone)
#           functions and classes in this module can be reused 
#           without the main block of code executing

# def main():

# if __name__ == '_main_':
#     main()








# emoji = win + ;



# apple = "banana"+"monkey"+ "blahbalha"

# apple = list(apple)
# print(apple)

#turend each character into an invidual element




#PYTHON OBJECT ORIENTED PROGRAMMING
#object = a "bundle" of related attributes (variables) and methods (functions)
#       ex. phone, cup,book
#       you need a "class" to create many objects
# class = (blueprint) used to design the structure and layout of an object

# note a method is a function that belongs in an object


# class car:
#     def __init__(self, model, year, color, for_sale): ##needed to construct object
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale

# from intr_class import car
# car1 = car("Mustang", 2025,"red", False)
# car2 = car("BMW", 2026, "blue", True)
# car3 = car("Charger", 2027, "yellow",True)

# print(car3.model)
# print(car3.year)
# print(car3.color)
# print(car3.for_sale)

# not class takes space soo we import into another file






#methods are actions that our objects can perform
#improting this to intr_class.
# class car:
#     def __init__(self, model, year, color, for_sale): ##needed to construct object
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale

#     def drive(self):
#         print("You drive the car")
#     def stop(self):
#         print("you stopped the car")

# from intr_class import car
# car1 = car("Mustang", 2025,"red", False)
# car2 = car("BMW", 2026, "blue", True)
# car3 = car("Charger", 2027, "yellow",True)

# car1.drive()
# car1.stop()
# print()
# car2.drive()
# car2.stop()
# print()
# car3.drive()
# car3.stop()


# car1.describe()
# car2.describe()
# car3.describe()




#class varaiables = shared among all instance of a class
#               defined outside the constructor
#                 allow you to share data among all objects created from that class


# class Student:
    
#     class_year = 2024
#     num_students = 0
    
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         Student.num_students += 1

# student1 = Student("dami", 49)
# student2 = Student("dola", 34)
# student3 = Student("SANDY",43)
# student4 = Student("life",44)
# print(student1.name)
# print(student1.age)
# print(student2.name)
# print(student2.age)
# print(student1.class_year)
# print(student2.class_year)
# print(Student.class_year)

# print(Student.num_students)




# Inheritance = Allows a class to inherit attributes and methods from another class
#             helps with code reusability and extensibility
#             class Child(Parent)



# class Animal:
#     def __init__(self,name):
#         self.name = name
#         self.is_alive = True
#     def eat(self):
#         print(f"{self.name} is eating")
#     def sleep(self):
#         print(f"{self.name} is sleeping")

# class Dog(Animal):
#     pass



# class Cat(Animal):
#     pass


# class Mouse(Animal):
#     pass



# dog = Dog("Daisy")
# cat = Cat("Tom")
# mouse = Mouse("Jerry")

# print(dog.name)
# print(dog.is_alive)
# dog.eat()
# dog.sleep()

# print(cat.name)
# print(cat.is_alive)
# cat.eat()
# cat.sleep()

# print(mouse.name)
# print(mouse.is_alive)
# mouse.eat()
# mouse.sleep()







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
#         print("WOOf")



# class Cat(Animal):
#     def speak(self):
#         print("MEOW")


# class Mouse(Animal):
#     def speak(self):
#         print("SQUEEK!")



# dog = Dog("Daisy")
# cat = Cat("Tom")
# mouse = Mouse("Jerry")

# dog.speak()
# cat.speak()
# mouse.speak()



#  multiple inheritance = inherit from more than one parent class
#                     C(A,B)


# multilevel inheritance = inherit from a parent which inherits from another parent 
#                   C(B) <- B(A) <- A



#multiple inheritance

# class Prey:
#     def flee(self):
#         print("This animal is fleeing")

# class Predator:
#     def hunt(self):
#         print("This animal is hunting")

# class Rabbit(Prey):
#     pass

# class Hawk(Predator):
#     pass

# class Fish(Prey,Predator):
#     pass


# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()

# rabbit.flee()
# hawk.hunt()
# fish.hunt()
# fish.flee()




# # multilevel inheritance

# class Animal:  #grandparent
#     def eat(self):
#         print("This animal is eating")
#     def sleep(self):
#         print("This animal is sleeping")

# class Prey(Animal): #parent
#     def flee(self):
#         print("This animal is fleeing")

# class Predator(Animal): # parent
#     def hunt(self):
#         print("This animal is hunting")

# class Rabbit(Prey): # children
#     pass

# class Hawk(Predator):  #children
#     pass

# class Fish(Prey,Predator):  #children
#     pass


# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()

# rabbit.flee()
# hawk.hunt()
# fish.hunt()
# fish.flee()

# rabbit.eat()
# rabbit.sleep()

# fish.eat()
# fish.sleep()

# hawk.sleep()
# hawk.eat()






# class Animal:  #grandparent
#     def __init__(self,name):
#         self.name = name
#     def eat(self):
#         print(f" {self.name} is eating")
#     def sleep(self):
#         print(f"{self.name} is sleeping")

# class Prey(Animal): #parent
#     def flee(self):
#         print(f"{self.name} is fleeing")

# class Predator(Animal): # parent
#     def hunt(self):
#         print(f"{self.name} is hunting")

# class Rabbit(Prey): # chilren
#     pass

# class Hawk(Predator):  #chilren
#     pass

# class Fish(Prey,Predator):  #chilren
#     pass


# rabbit = Rabbit("Bugs")
# hawk = Hawk("Tony")
# fish = Fish("Nemo")

# rabbit.flee()
# hawk.hunt()
# fish.hunt()
# fish.flee()

# rabbit.eat()
# rabbit.sleep()

# fish.eat()
# fish.sleep()

# hawk.sleep()
# hawk.eat()













# super () = Function used in a child class to call methods from a parents class (superclass)
#               Allows you to extend the functionality of the inherited methods


# class Shape:
#     def __init__(self,color,is_filled):
#         self.color = color
#         self.is_filled = is_filled

#     def describe(self):
#         print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

# class Circle(Shape):
#     def __init__(self,color,is_filled,radius):
#         super().__init__(color,is_filled)
#         self.radius = radius

#     def describe(self):  
#         super().describe()
#         print(f"It is a circle with an area of {3.14*self.radius*self.radius}cm^2")
        
        

# class Square(Shape):
#     def __init__(self,color,is_filled,width):
#        super().__init__(color,is_filled)
#        self.width = width
#     def describe(self):  
#         super().describe()
#         print(f"It is a square with an area of {self.width*self.width}cm^2")
        


# class Triangle(Shape):
#    def __init__(self,color,is_filled,width,height):
#         super().__init__(color,is_filled)
        
#         self.width = width
#         self.height = height

#    def describe(self): 
#         super().describe()
#         print(f"It is a triangle with an area of {self.width*self.height}cm^2")
        




# circle = Circle(color="Red", is_filled=True,radius=7)
# square = Square(color="Blue", is_filled=False, width=19)
# triangle = Triangle(color="Green", is_filled=True,width=9, height=38)

# # print(circle.color)
# # print(circle.is_filled)
# # print(f"{circle.radius:.2f}")
# # print()
# # print(square.color)
# # print(square.is_filled)
# # print(f"{square.width:.2f}")
# # print()
# # print(triangle.color)
# # print(triangle.is_filled)
# # print(f"{triangle.width:.2f}")
# # print(f"{triangle.height:.2f}")



# # circle.describe()
# # triangle.describe()
# # square.describe()

# circle.describe()
# square.describe()
# triangle.describe()




# Polymorphism = Greek word that means to "have many forms or faces"
#                   poly = Many
#                   morphe = form

#                   Two WAYS TO ACHIEVE POLYMORPHISM
#                   1. Inheritance = An object could br treated of the same type as a parent class
#                   2. "Duck Typing" = Object must have necessary attributes/methods


# # inheritance
# from abc import ABC, abstractmethod
# class Shape:
    
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
      
#     def area(self):
#         return 3.14 * self.radius **2

# class Square(Shape):
#     def __init__(self,side):
#         self.side = side
      
#     def area(self):
#         return  self.side **2
        

# class Triangle(Shape):
#     def __init__(self,base,height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return self.base * self.height * 0.5
    
# class Pizza(Circle):
#     def __init__(self,topping,radius):
#         super().__init__(radius)
#         self.topping = topping
        

# shapes = [Circle(3), Square(5), Triangle(6,7), Pizza("mushroom", 23)]
# for shape in shapes:
#     print(f"{shape.area()}cm^2")

# # circle = Circle()
# # square = Square()
# # triangle = Triangle()





#"Duck Typing" = Another way to achieve polymorphism besides Ingeritance
#                   object must haver the minimum necessary attributes/methods
#                    "if it looks like a duck and quacks like a duck, it must be a duck"



# class Animal:
#     alive = True



# class Dog(Animal):
#     def speak(self):
#         print("WOOF!")

# class Cat(Animal):
#     def speak(self):
#         print("MEOW!!")

# class Car:
#     alive = False
#     def speak(self):
#         print("HONK!!")

# animals =[Dog(),Cat(),Car()]

# # here we see that Car is not parent of the class Animal
# #  buh becuz it as the same "speak" method it will print with the others
# for animal in animals:
#     animal.speak()
#     print(animal.alive)



# Static methods =  A method that belong to a class rather than any object from that class (intance )
#                     Usually used for general utility functions

# Instance methods = Best for operations on instances of the class (objects)
#   Static methods =  Best for utility functions that do not need access to class data


# class Employee:
    
#     def __init__(self,name,positon):
#         self.name = name
#         self.position = positon
# #Instance method
#     def get_info(self):
#         return f"{self.name} = {self.position}"
    
#   #Static method
#     @staticmethod
#     def is_valid_postion(postion):
#         valid_postions = ["Manager","Cashier", "Cook", "Janitor"]
#         return postion in valid_postions


# #for instance method
# employee1 = Employee("Eugune", "Manager")
# employee2 = Employee("Squidward", "Cashier")
# employee3 = Employee("Spongebob", "Cook")
# print(employee1.get_info())
# print(employee2.get_info())
# print(employee3.get_info())

# #for static
# print(Employee.is_valid_postion("Cook"))
# print(Employee.is_valid_postion("Rocket Scientist"))   


# Class methods = Allow operations relted to the class itself
#                  Take (cls) at the first parameter, which represents the class itself 


# class Student:
#     count = 0 
#     total_gpa = 0
#     def __init__(self,name,gpa):
#         self.name = name
#         self.gpa = gpa
#         Student.count += 1
#         Student.total_gpa += gpa
#      #INSTANCE METHOD
#     def get_info(self):
#         return f"{self.name} {self.gpa}"
    

#     #CLASS METHOD
#     @classmethod
#     def get_count(cls):
#         return f"Total # of student: {cls.count}"
    
#     @classmethod
#     def get_average_gpa(cls):
#         if cls.count == 0:
#             return 0
#         else:
#             return f"Average gpa: {cls.total_gpa / cls.count:.2f}"

# student1 = Student("Spongebob", 3.3)
# student2 = Student("Squidward", 5)
# student3 = Student("Eugene", 4.3)
# print(Student.get_count())
    
# print(Student.get_average_gpa())


# # Instance methods =  Best for operations on instances of the class (objects)
# # Static methos =  Best for utilitu functions that do not need access to class data
# # Class methods =  Best for class- level data or require access to the class itself








# # Magic methods =  Dunder methods (double underscore) __init__, __str__,__eq__
# #               they are automatically called by many of python's built-in operations
# #               they allow developers to define or customize the behavor of objecs

# class Book:
    
#     def __init__(self,title,author,num_pages):
#         self.title = title
#         self.author = author
#         self.num_pages = num_pages
    
#     def __str__(self): #this enable it to print directly
#         return f"'{self.title}' by {self.author}"
#     def __eq__(self, other): # compares if two objects are equal
#         return self.title == other.title and self.author == other.author
#     def __lt__(self,other):
#         return self.num_pages < other.num_pages
#     def __add__(self, other):
#         return f"{self.num_pages + other.num_pages} pages"
#     def __contains__(self,keyword):
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
# book1 = Book("The Hobbit","J.R.R. Tolkien", 310)
# book2 = Book("Harry Potter and The Philsopers Stone", "J.K Rowling", 233)
# book3 = Book("The Lion, The Witch and the Wardrobe", "C.S. Lewis", 174)

# # print(book1)
# # print(book2)
# # print(book3)


# # print(book1 == book2)
# # print(book2 < book3)
# # print(book2 > book3)
# # print(book2 + book3)


# # print("Lion"in book1)
# # print("Potter"in book2)

# print(book3['author'])
# print(book3['num_pages'])











# @property = Decorator used to define a method as a property(it can be accessed like an attribute)
#               Benefit: Add additional logic when read, write, or delete attributes
#                Gives you getter, setter and deleter method
#              getter = read, setter = write, deleter = delete



# class Rectangle:
#     def __init__(self,width, height):
#         self._width = width  # self._width = means it is a private it tells you not access it directly outside of the class
#         self._height = height
     
#     @property
#     def width(self):
#         return f"{self._width:.1f}cm"    # <--- getter method

#     @property
#     def height(self):
#         return f"{self._height:.1f}cm"
    
#     @width.setter                   # <------- setter method
#     def width(self,new_width):
#         if new_width > 0 :
#             self._width = new_width
#         else:
#             print("Width must be greater than zero")
    
#     @height.setter
#     def height(self,new_height):
#         if new_height > 0 :
#             self._height= new_height
#         else:
#             print("Height must be greater than zero")

#     @width.deleter   #              <------- deleter method
#     def width(self):
#         del self._width
#         print("Width has been deleted")
#     @height.deleter
#     def height(self):
#         del self._height
#         print("Height has been deleted")



# rectangle = Rectangle(3,5)
# rectangle.width = 6
# rectangle.height = 8
# print(rectangle.width)
# print(rectangle.height)
# del rectangle.width
# del rectangle.height






# Decorator = A function that extends the behavior of another function
#               without modifying the base function
#               pass the base function as an argument to the decorator


#                @add_sprinkles
#                 get_ice_cream("vanilla")


# def add_sprinkles(func):
#     def wrapper(*args, **kwargs):
#         print("*You add sprinkles 🎊 *")

#         func(*args, **kwargs)
#     return wrapper
# def add_fudge(func):
#     def wrapper(*args, **kwargs):
#         print("* You add fudge *")
#         func(*args, **kwargs)
#     return wrapper


# @add_sprinkles
# @add_fudge
# def get_ice_cream(flavour):
#     print(f"Here is your {flavour} ice cream 🍨")


# get_ice_cream("Vanilla")




#exception = An  event that interrupts the flow of a program
#           (ZeroDivisionError, TypeError, ValueError)
#             1. try, 2.except, 3.finally

#1/0 - this gives a ZeroDivisionError; diving a number by 0
# 1 + "1" - this gives TypeError; trying to operate on avalue of a wrong datatype
# int("pizza") - this gives ValueError; trying to type cast a data with a wrong data type



# try -  any code that might be dangerous where it could cause an error. you will place within a try block

# number = int(input("Enter a number: "))
# print(1/number)

# this particular code is dangerous becuz the user might enter 0, or a word. 
# so we place it in  a try block



# try:
#     number = int(input("Enter a number: "))
#     print(1/number) 
# # note after a try block there should be an except block 
# except ZeroDivisionError:
#     print("You Can't divide by zero")
# except ValueError:
#     print("Enter only numbers")
# # or
# except Exception:  
#     print("SOmething went wrong")

# finally:   # it always execute reardless of any expections
#     print("Do some clean up")

    





# Python file detection
#created a text.txt
# import os
# file_path = "stuff/test.txt"  #relative 
# file_path2 = "C:/Users/DARAMZ/Desktop/test.txt" # absolute
# # if os.path.exists(file_path):
# #     print(f"The location {file_path} exists")
# # else:
# #     print("That location doesn't exist")
# if os.path.exists(file_path2):
#     print(f"The location {file_path2} exists")
# else:
#     print("That location doesn't exist")


# import os

# file_path = "C:/Users/DARAMZ/Desktop/test.txt" 
# if os.path.exists(file_path):
#     print(f"The location {file_path} exists")

#     if os.path.isfile(file_path):
#         print("That is a file")
#     elif os.path.isdir(file_path):
#         print("That is a directory")
# else:
#     print("That location doesn't exist")




# #Python writing files(.txt, .json, .csv)
# txt_data = "I like pizza!"

# file_path = "output.txt"

# with open(file_path, "w") as file:  #to create a file
#     # with is a statement used to wrap a block of code to execute
#     # when we open a file the with statement closes that file when we're done with it
#     # the open function will return a file object 
#     # the first parameter is the file_path
#     # the second parameter is the mode;
#     # "w" - write
#     # "x" - it also write if the "output.txt" doesn't exists
#     # "a" - append; to append a file
#     # "r" - to read


#     file.write(txt_data)
#     print(f"txt file {file_path} was created")




# txt_data = "I like pizza!"

# file_path = "C:/Users/DARAMZ/Desktop/output.txt"
# with open(file_path, "w") as file:
#     file.write(txt_data)
#     print(f"txt file {file_path} was created")


# txt_data = "I like pizza!"

# file_path = "C:/Users/DARAMZ/Desktop/output.txt"

# try:
#   with open(file_path, "x") as file:  #x
#       file.write(txt_data)
#       print(f"txt file {file_path} was created")

# except FileExistsError:
#    print("That file already exists")




# txt_data = "I like pizza!"

# file_path = "C:/Users/DARAMZ/Desktop/output.txt"

# try:
#   with open(file_path, "a") as file:  #a
#       file.write("\n"+ txt_data)
#       print(f"txt file {file_path} was created")

# except FileExistsError:
#    print("That file already exists")





# employees = ["Eugene", "Spongebob", "Squidward", "Patrick"]

# file_path = "C:/Users/DARAMZ/Desktop/output.txt"

# try:
#   with open(file_path, "w") as file:  #x
#       for employee in employees:
#          file.write(employee + " ")
#       print(f"txt file {file_path} was created")

# except FileExistsError:
#    print("That file already exists")




# .json  collect of key value pairs
# import json
# employee = {
#    "name": "Spongebob", 
#    "age" : 30,
#    "job" : "Fry cook"}

# file_path = "C:/Users/DARAMZ/Desktop/output.json"

# try:
#   with open(file_path, "w") as file:  
#       json.dump(employee, file, indent=4)
#       print(f"jsont file {file_path} was created")

# except FileExistsError:
#    print("That file already exists")




# # .csv - comma separated values (COMMON IN EXCEL DATA SHEET)
# import json
# import csv
# employee = [["Name","Age","Job"],
#             ["Spongebob",30,"Cook"],
#             ["Patrick",38, "UNemployed"],
#             ["Sandy", 27, "Scientist"]]
# file_path = "C:/Users/DARAMZ/Desktop/output.csv"

# try:
#   with open(file_path, "w", newline="") as file:  
#       writer = csv.writer(file)
#       for row in employee:
#          writer.writerow(row)
#       print(f"csv file {file_path} was created")

# except FileExistsError:
#    print("That file already exists")



# Python reading files(.txt, .json, .csv)
# .txt
# file_path = "C:/Users/DARAMZ/Desktop/output.txt"

# try:
#   with open(file_path, "r") as file:
#       content = file.read()
#       print(content)
# except FileNotFoundError:
#    print("That file was not found")
# except PermissionError:
#    print("You are not granted permission")



# #.json
# import json
# file_path = "C:/Users/DARAMZ/Desktop/output.json"

# try:
#   with open(file_path, "r") as file:
#       content = json.load(file)
#       print(content)
#       print(content["name"])
#       print(content["job"])
#       print(content["age"])
# except FileNotFoundError:
#    print("That file was not found")
# except PermissionError:
#    print("You are not granted permission")



# # .csv
# import csv
# file_path = "C:/Users/DARAMZ/Desktop/output.csv"

# try:
#   with open(file_path, "r") as file:
#       content = csv.reader(file)
#       for line in content:
#          print(line)
      
      
# except FileNotFoundError:
#    print("That file was not found")
# except PermissionError:
#    print("You are not granted permission")








# dates & times

# import datetime

# date = datetime.date(2025,1,2)   # (2025-year,1-month,2-day)
# today  = datetime.date.today()
# print(date)
# print(today)

# time = datetime.time(12,30,0) # (12-hour,30-min, 0 - secs)
# now = datetime.datetime.now() # this returns a date and time
# now = now.strftime("%H:%M:%S  %m-%d-%Y")
# print(time)
# print(now)



# import datetime


# target_datetime = datetime.datetime(2030,2,23, 12,30,1)
# current_datetime = datetime.datetime.now()

# if target_datetime < current_datetime:
#     print("Target date has passed")
# else:
#     print("Target date has NOT passed")




# multithreading = used to perform tasks concurrently (multitasking)
#                   good for input/output tasks
#                   to use - threading.Thread(target=my_function)



# import threading
# import time

# def walk_dog(first, last):
#     time.sleep(8)
#     print(f"You finish walking the {first} {last}")
  
# def take_out_trash():
#     time.sleep(2)
#     print("You take out the trash")


# def get_mail():
#     time.sleep(4)
#     print("You get the mail")


# chore1 = threading.Thread(target=walk_dog, args=("Scooby" , "Doo"))
# chore1.start()
# chore2 = threading.Thread(target=take_out_trash)
# chore2.start()
# chore3 = threading.Thread(target=get_mail)
# chore3.start()


# chore1.join()
# chore2.join()
# chore3.join()
# print("All chores are complete")



# # How to connect to an API using Python
# #API - Application Programming Interface

# import requests

# base_url = "https://pokeapi.co/api/v2/"

# def get_pokemon_info(name):
#     url = f"{base_url}/pokemon/{name}"
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         pokemon_data = response.json()
#         return pokemon_data
#     else:
#         print(f"Falied to retrieve data {response.status_code}")
# pokemon_name = "Typhlosion"
# pokemon_info = get_pokemon_info(pokemon_name)

# if pokemon_info: 
#     print(f"Name: {pokemon_info["name"].capitalize()}")
#     print(f"Id: {pokemon_info["id"]}")
#     print(f"Height: {pokemon_info["height"]}")
#     print(f"Weight: {pokemon_info["weight"]}")







# PyQt5
# #GUI intro 
# # #how to create windows
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5.QtGui import QIcon
# class MainWndow(QMainWindow): 
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("My First GUI")
#         self.setGeometry(500, 200, 500, 500)
#         self.setWindowIcon(QIcon("aizen.jpg"))
    

# def main():
#     app = QApplication(sys.argv)
#     window = MainWndow()
#     window.show()
#     sys.exit(app.exec_())



# if __name__ == "__main__":
#     main()



# # creating labels
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
# from PyQt5.QtGui import QFont
# from PyQt5.QtCore import Qt
# class MainWndow(QMainWindow): 
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("My First GUI")
#         self.setGeometry(700, 300, 500, 500)
#         label = QLabel("Hello", self)
#         label.setFont(QFont("Arial", 40))
#         label.setGeometry(0,0, 500, 100)
#         label.setStyleSheet("color: red;" 
#                             "background-color: #6fdcf7;"
#                             "font-weight: bold;"
#                             "font-style: italic;"
#                             "text-decoration: underline;")
#         # label.setAlignment(Qt.AlignTop) # Vertically top
#         # label.setAlignment(Qt.AlignBottom) # Vertically bottom
#         # label.setAlignment(Qt.AlignVCenter) # Vertically Center


#         # label.setAlignment(Qt.AlignRight) #Horizontally Right
#         # label.setAlignment(Qt.AlignHCenter) #Horizontally Center
#         # label.setAlignment(Qt.AlignLeft) #horizontally left

#         # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) #Center & top
#         # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) #Center & Bottom
#         # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # Center & center

#         label.setAlignment(Qt.AlignCenter) # Center & center




# def main():
#     app = QApplication(sys.argv)
#     window = MainWndow()
#     window.show()
#     sys.exit(app.exec_())



# if __name__ == "__main__":
#     main()




#PyQt5 images


# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
# from PyQt5.QtGui import QPixmap

# class MainWndow(QMainWindow): 
#     def __init__(self):
#         super().__init__()
        
#         self.setGeometry(700, 300, 500, 500)

#         label= QLabel(self)
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
#     window = MainWndow()
#     window.show()
#     sys.exit(app.exec_())



# if __name__ == "__main__":
#     main()


# #PyQt5  Layout
# import sys
# from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget,
#                             QVBoxLayout, QHBoxLayout, QGridLayout)

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(500,200,500,500)
#         self.setWindowTitle("Layout Managers")

#         self.initUI()


#     def initUI(self):
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)

#         label1 = QLabel("#1", self)
#         label2 = QLabel("#2", self)
#         label3 = QLabel("#3", self)
#         label4 = QLabel("#4", self)
#         label5 = QLabel("#5", self)

#         label1.setStyleSheet("background-color: red;")
#         label2.setStyleSheet("background-color: yellow;")
#         label3.setStyleSheet("background-color: green;")
#         label4.setStyleSheet("background-color: blue;")
#         label5.setStyleSheet("background-color: purple;")


#         grid= QGridLayout()

#         grid.addWidget(label1, 0, 0)  # (0,0, == row, column)
#         grid.addWidget(label2, 0, 1)
#         grid.addWidget(label3, 1,0)
#         grid.addWidget(label4, 1,1)
#         grid.addWidget(label5, 2,2)

#         central_widget.setLayout(grid)
       
        

    
    
# def main():
#     application = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(application.exec_())

# if __name__ == "__main__":
#     main()



# # # PyQt5   buttons

# import sys
# from PyQt5.QtWidgets import (QApplication,QMainWindow, QLabel, QPushButton)


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(500,200, 500,500)
#         self.button = QPushButton("Click me!", self)
#         self.label = QLabel("Hello", self)

#         self.initUI()

#     def initUI(self):
        
#         self.button.setGeometry(150,200,200,100)
#         self.button.setStyleSheet("font-size: 30px;")
#         self.button.clicked.connect(self.on_click)
#         # self.button.setDisabled(True)

#         self.label.setGeometry(150,300,200,100)
#         self.label.setStyleSheet("font-size: 50px;")

#     def on_click(self):
#         self.label.setText("Goodbye")

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()









# # PyQt5   CheckBoxes

# import sys
# from PyQt5.QtWidgets import (QApplication,QMainWindow, QLabel, QCheckBox)
# from PyQt5.QtCore import Qt


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(500,200, 500,500)
#         self.checkbox = QCheckBox("Do you Like food?", self)
#         self.initUI()

#     def initUI(self):
#         self.checkbox.setGeometry(10,0, 500, 100)
#         self.checkbox.setStyleSheet("font-size: 30px; " \
#         "font-family: Arial;")
#         self.checkbox.setChecked(False)

#         self.checkbox.stateChanged.connect(self.checkbox_changed)

#     def checkbox_changed(self, state):
#         if state == Qt.Checked:
#             print("You like food")
#         else:
#             print("You do not like food")
    



# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()





# # PyQt5   radio buttons

# import sys
# from PyQt5.QtWidgets import (QApplication,QMainWindow, QRadioButton, QButtonGroup)


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(500,200, 500,500)
#         self.radio1 = QRadioButton("Visa", self)
#         self.radio2 = QRadioButton("Mastercard", self)
#         self.radio3 = QRadioButton("Giftcard", self)
#         self.radio4 = QRadioButton("In-Store", self)
#         self.radio5 = QRadioButton("Online", self)
#         self.button_group1 = QButtonGroup(self)
#         self.button_group2 = QButtonGroup(self)
        
#         self.initUI()

#     def initUI(self):
#         self.radio1.setGeometry(0,0, 300, 50)
#         self.radio2.setGeometry(0,50, 300, 50)
#         self.radio3.setGeometry(0,100, 300, 50)
#         self.radio4.setGeometry(0,150, 300, 50)
#         self.radio5.setGeometry(0,200, 300, 50)

#         self.setStyleSheet("QRadioButton{" \
#         "                        font-size: 40px;" \
#         "                         font-family: Arial;" \
#         "                         padding: 10px;}")

#         self.button_group1.addButton(self.radio1)
#         self.button_group1.addButton(self.radio2)
#         self.button_group1.addButton(self.radio3)

#         self.button_group2.addButton(self.radio4)
#         self.button_group2.addButton(self.radio5)


#         self.radio1.toggled.connect(self.radio_button_changed)
#         self.radio2.toggled.connect(self.radio_button_changed)
#         self.radio3.toggled.connect(self.radio_button_changed)
#         self.radio4.toggled.connect(self.radio_button_changed)
#         self.radio5.toggled.connect(self.radio_button_changed)
       




#     def radio_button_changed(self):
#         radio_button = self.sender()
#         if radio_button.isChecked():
#             print(f"{radio_button.text()} is selected")
        

# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()




# # TextBoxes

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(500,200,500,500)
#         self.line_edit = QLineEdit(self)
#         self.button = QPushButton("Submit", self)


#         self.initUI()
    
#     def initUI(self):
#         self.line_edit.setGeometry(10,10, 200, 40)
#         self.button.setGeometry(210, 10, 100, 40)
#         self.button.setStyleSheet("font-size: 25px; font family: Arial;")
#         self.line_edit.setStyleSheet("font-size: 25px; font family: Arial;")
#         self.line_edit.setPlaceholderText("Enter your name ")


#         self.button.clicked.connect(self.submit)

#     def submit(self):
#         text = self.line_edit.text()
#         print(f"Hello {text}")





# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()




# # PyQt5 CSS Styles

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QHBoxLayout

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.button1 = QPushButton("#1")
#         self.button2 = QPushButton("#2")
#         self.button3 = QPushButton("#3")
#         self.InitUI()
#     def InitUI(self):
#         central_widgit = QWidget()
#         self.setCentralWidget(central_widgit)
#         Hbox = QHBoxLayout()
#         central_widgit.setLayout(Hbox)

#         self.button1.setObjectName("button1")
#         self.button2.setObjectName("button2")
#         self.button3.setObjectName("button3")


#         Hbox.addWidget(self.button1)
#         Hbox.addWidget(self.button2)
#         Hbox.addWidget(self.button3)


#         self.setStyleSheet(""" QPushButton{
#                            font-size: 40px;
#                            font-family: Arial;
#                            padding: 15px 75px;
#                            margin: 25px;
#                            border: 3px solid;
#                            border-radius: 15px;
#                            }
                           
#                            QPushButton#button1{
#                            background-color: red;
#                            color: white;

#                            } 
#                            QPushButton#button2{
#                            background-color: green;
#                            color: yellow;
                           
#                            } 
#                            QPushButton#button3{
#                            background-color: blue;
#                            color: pink;
                           
#                            }
                           
#                            QPushButton#button1:hover{
#                            background-color: hsl(0, 100%, 84%);
#                            color: grey;

#                            } 
#                            QPushButton#button2:hover{
#                            background-color: hsl(122, 100%, 84%);
#                            color: purple;
                           
#                            } 
#                            QPushButton#button3:hover{
#                            background-color: hsl(204, 100%, 84%);
#                            color: white;
                           
#                            } """)



        
        


# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()





# # Digital CLock

# import sys
# from PyQt5.QtWidgets import QApplication,  QLabel, QWidget, QVBoxLayout
# from PyQt5.QtCore import QTime, QTimer, Qt
# from PyQt5.QtGui import QFont, QFontDatabase
# class DigitalClock(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(600,400,300,100)
#         self.time_label = QLabel(self)
#         self.timer = QTimer(self)
#         self.initUI()
     
#     def initUI(self):
#         self.setWindowTitle("DIGITAL CLOCK")

#         vbox = QVBoxLayout()
        
#         vbox.addWidget(self.time_label)

#         self.setLayout(vbox)
#         self.time_label.setAlignment(Qt.AlignCenter)

#         self.timer.timeout.connect(self.update_time)
#         self.timer.start(1000)

#         self.time_label.setStyleSheet("font-size: 150px;  color: hsl(111, 100%, 50%);")
#         self.setStyleSheet("background-color: black;")

#         font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
#         font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
#         my_font = QFont(font_family, 150)
#         self.time_label.setFont(my_font)
        
#         self.update_time()

#     def update_time(self):
#         current_time = QTime.currentTime().toString("hh:mm:ss AP")
#         self.time_label.setText(current_time)
        


# def main():
#     app = QApplication(sys.argv)
#     window = DigitalClock()
#     window.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()








# # Python PyQt5 Stopwatch
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton,QVBoxLayout, QHBoxLayout
# from PyQt5.QtCore import QTimer, QTime, Qt
# class Stopwatch(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(600,400,300,100)
#         self.setWindowTitle("STOPWATCH")
#         self.time = QTime(0, 0, 0, 0)
#         self.time_label = QLabel("00:00:00", self)
#         self.start_button = QPushButton("Start", self)
#         self.stop_button = QPushButton("Stop", self)
#         self.reset_button = QPushButton("Reset", self)
#         self.timer = QTimer(self)

#         self.initUI()
      
#     def initUI(self):
#         vbox =QVBoxLayout()
#         vbox.addWidget(self.time_label)
       
#         self.setLayout(vbox)
#         self.time_label.setAlignment(Qt.AlignCenter)

#         hbox = QHBoxLayout()
#         hbox.addWidget(self.start_button)
#         hbox.addWidget(self.stop_button)
#         hbox.addWidget(self.reset_button)

#         vbox.addLayout(hbox)
#         self.setStyleSheet(
#             """
#             QPushButton, QLabel{
#               padding: 20px;
#               font-weight: bold;
#               font-family: calibri;
#             }
#             QPushButton{
#               font-size: 50px;

#             }
#             QLabel{
#               font-size: 120px;
#               background-color: hsl(200, 100%, 85%);
#               border-radius: 20px;
#               }
#             """)
        
#         self.start_button.clicked.connect(self.start)
#         self.stop_button.clicked.connect(self.stop)
#         self.reset_button.clicked.connect(self.reset)
#         self.timer.timeout.connect(self.update_display)
        

#     def start(self):
#         self.timer.start(10)
    
#     def stop(self):
#         self.timer.stop()
    
#     def reset(self):
#         self.timer.stop()
#         self.time = QTime(0, 0, 0, 0,)
#         self.time_label.setText(self.format_time(self.time))
    
#     def format_time(self, time):
#         hours = time.hour()
#         minutes = time.minute()
#         seconds = time.second()
#         milliseconds = time.msec() // 10
#         return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"
    
#     def update_display(self):
#         self.time = self.time.addMSecs(10)
#         self.time_label.setText(self.format_time(self.time))



# def main():
#     app = QApplication(sys.argv)
#     window = Stopwatch()
#     window.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()





# WeatherApp


# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
# from PyQt5.QtCore import Qt
# import requests
# class Weather_app(QWidget):
#     def __init__(self):
#         super().__init__()
       
#         self.setWindowTitle("Weather App")
#         self.city_label = QLabel("Enter City Name: ", self)
#         self.city_input = QLineEdit(self)
#         self.get_weather_button = QPushButton("GET WEATHER", self)
#         self.temperture_label = QLabel(self)
#         self.emoji_label = QLabel(self)
#         self.description_label = QLabel(self)
#         self.initUI()


#     def initUI(self):
#         vbox = QVBoxLayout()
#         vbox.addWidget(self.city_label)
#         vbox.addWidget(self.city_input)
#         vbox.addWidget(self.get_weather_button)
#         vbox.addWidget(self.temperture_label)
#         vbox.addWidget(self.emoji_label)
#         vbox.addWidget(self.description_label)

#         self.setLayout(vbox)


#         self.city_label.setAlignment(Qt.AlignCenter)
#         self.city_input.setAlignment(Qt.AlignCenter)
#         self.temperture_label.setAlignment(Qt.AlignCenter)
#         self.emoji_label.setAlignment(Qt.AlignCenter)
#         self.description_label.setAlignment(Qt.AlignCenter)


#         self.city_label.setObjectName("city_label")
#         self.city_input.setObjectName("city_input")
#         self.get_weather_button.setObjectName("get_weather_button")
#         self.temperture_label.setObjectName("temperture_label")
#         self.emoji_label.setObjectName("emoji_label")
#         self.description_label.setObjectName("description_label")



#         self.setStyleSheet(
#             """ 
#             QLabel, QPushButton{
#               font-family: calibri;
#             }

#             QLabel#city_label{
#               font-size: 40px;
#               font-style: italic;
#             }

#             QLineEdit#city_input{
#               font-size: 40px;
              
#             }

#             QPushButton#get_weather_button{
#               font-size:30px;
#               font-weight: bold;
#             }

#             QLabel#temperture_label{
#               font-size: 75px;
              
#             }
            
#             QLabel#emoji_label{
#             font-size: 100px;
#             font-family: Segoe UI emoji}

#             QLabel#description_label{
#             font-size: 100px;
#             }

            

#             """
#         )

#         self.get_weather_button.clicked.connect(self.get_weather)
      

#     def get_weather(self):
#         api_key = "66fe1e0a913f74e45e2b55035e41704f"
#         city = self.city_input.text()
#         url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"


#         try:
#           response = requests.get(url)
#           response.raise_for_status()
#           data = response.json()

#           if data["cod"] == 200:
#               self.display_weather(data)

#         except requests.exceptions.HTTPError as http_error:
#             match response.status_code:
#                 case 400:
#                     self.display_error("Bad request:\n Please Check your input")
#                 case 401:
#                     self.display_error("Unauthorized:\n Invalid API key")
#                 case 403:
#                     self.display_error("Forbidden:\n Access is denied")
#                 case 404:
#                     self.display_error("Not Found: \nCity not found")
#                 case 500:
#                    self.display_error("Internal Server Error: \n Please Check your input")
#                 case  502:
#                     self.display_error("Bad Gateway: \n Please Invalid response from the server")
#                 case 503:
#                    self.display_error("Service Unavailable: \n Server is down")
#                 case 504:
#                     self.display_error("Gateway Timeout: \n No response from the server")
#                 case _:
#                     self.display_error(f"HTTP error occurred: \n {http_error}") 
#         except requests.exceptions.ConnectionError:
#             self.display_error("Connection error: \n Please check your network connection.")
#         except requests.exceptions.Timeout:
#             self.display_error("Timeout error: \n The request times out")
            
#         except requests.exceptions.TooManyRedirects:
#             self.display_error("Too many Redirects:\n Check your URL")

        

#         except requests.exceptions.RequestException as req_error:
#             self.display_error(f"Request Error:\n {req_error}")
            
    
    

#     def display_error(self, message):
#         self.temperture_label.setStyleSheet("font-size: 30px;")
#         self.temperture_label.setText(message)
#         self.emoji_label.setText("")
#         self.description_label.setText("")
    

#     def display_weather(self, data):
#         self.temperture_label.setStyleSheet("font-size: 75px;")
#         temperature_k = data["main"] ["temp"]
#         temperature_c = temperature_k - 273.15
#         temperature_f = (temperature_k * 9/5) - 459.67
#         weather_id = data["weather"][0]["id"]
#         weather_description = data["weather"][0]["description"]
        
        


#         self.temperture_label.setText(f"{temperature_f:.2f} °F")
#         self.emoji_label.setText(self.get_weather_emoji(weather_id))
#         self.description_label.setText(weather_description.capitalize())

#     @staticmethod
#     def get_weather_emoji(weather_id):
#         if 200 <= weather_id <= 232:
#             return "⛈️"
#         elif 300 <= weather_id <= 321:
#             return "🌦️"
#         elif 500 <= weather_id <= 531:
#             return "🌧️"
#         elif 600 <= weather_id <= 622:
#             return "❄️"
#         elif 701 <= weather_id <= 781:
#             return "🌫️"
#         elif weather_id == 762:
#             return "🌋"
#         elif weather_id == 781:
#             return "🌪️"
#         elif weather_id == 800:
#             return "☀️"
#         elif 801 <= weather_id <= 804:
#             return "☁️"
#         else:
#             return "❓"

        


# def main():
#     app = QApplication(sys.argv)
#     window = Weather_app()
#     window.show()
#     sys.exit(app.exec_())


# if __name__ == "__main__":
#     main()





