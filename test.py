#AREA OF RECTANGLE CALC
#print ("AREA OF RECTANGLE CALC")
#length = float(input("ENTER THE LENGTH: "))
#width = float(input("ENTER THE WIDTH: "))
#area= length * width
#print(f"THE AREA OF THE RECTANGLE IS {area}")


#AREA OF A CIRCLE
#print ("CIRCUMFERENCE OF A CIRCLE")
#radius = float(input("ENTER THE RADIUS "))
#hi=22/7
#CIRCUMFERENCE = hi*radius*radius

#print(f"CIRCUMFERENCE OF THE CIRCLE IS {CIRCUMFERENCE} ")


#SHOPPING CART PROGRAM
#item= input("WHAT ITEM WOULD YOU LIKE TO BUY?! ")
#price = float(input("WHAT IS THE PRICE?! "))
#quantity = int(input("how many would you like?! "))

#total = price * quantity

#print(f"${total}")


#CIRCUMFERENCE OF A CIRCLE 
#import math

#print("CIRCUMFERENCE OF A CIRCLE ")
#radius = float(input("enter the radius of the circle: "))
#CIRCUMFERENCE =  2 * math.pi * radius
#rint(f"The CIRCUMFERENCE OF THE CIRCLE IS {round(CIRCUMFERENCE, 2)}cm ")


#AREA OF A CIRCLE 
#import math

#print("AREA OF A CIRCLE PART 2")
#radius = float(input(" enter radius: "))
#area = math.pi * pow(radius, 2)
#print(f"THE AREA OF THE CIRCLE IS: {round(area, 3)}cm")




#hypotense of right angle triangle
#import math

#print("hypotense of a right angle triangle")

#a = float(input("enter length: "))
#b = float(input("enter base: "))

#w = pow(a,2) + pow(b,2)
#c = math.sqrt(w)
#or
#c = math.sqrt(pow(a,2) + pow(b,2) )
#print(f"the hypotense of the riangle is : {round(c,2)}")



#validate userinput/username

# username = input("ENTER A USERNAME: ")
# if len(username) > 12:
#    print("YOUR USERNAME CANT BE MORE THAN 12 CHARACTERS")
# elif not username.find(" ") == -1:
#    print("username cant contain spaces")
# elif not username.isalpha():
#    print("your username cant contain numbers")
# else:
#    print(f"WELCOME {username}")


#compound interest calculator
# principal = 0
# rate = 0
# time = 0

# while principal <= 0:
#     principal = float(input("Enter the prinicipal amount: "))
#     if principal <= 0:
#         print("principal cant be less than or equal to zero(0)")

# while rate <= 0:
#     rate = float(input("Enter the interest amount: "))
#     if rate <= 0:
#         print("interest cant be less than or equal to zero(0)")

# while time <= 0:
#     time = int(input("Enter the time in years: "))
#     if time <= 0:
#         print("time cant be less than or equal to zero(0)")

        
# total = principal * pow((1 + rate/100), time)
# print(f"Balance after {time}years: ${total:.2f}")




#shopping cart program
# foods = []
# prices = []
# total = 0

# while True:
#     food = input("enter a food to buy/add to cart (type q to quit): ")
#     if food.lower() == "q":
#         print("thank you")
#         break
#     else: 
#         price = float(input(f"ENTER THE PRICE OF {food}: $"))
#         foods.append(food)
#         prices.append(price)

# print("------- your cart-----")

# for food in foods:
#     print(food, end=" ")
# for price in prices:
#         total += price
#         print(total, end=" ")
# print()
# print(f"your total is {total}")





#two dimensinal keyboard
# num_pad = ((1, 2, 3),
#            (4, 5, 6),
#              (7, 8, 9),
#                ("*",0,"#"))
# for row in num_pad:
    
#     for num in row:
#         print(num, end=" ")
#     print()




# #quiz game


questions =(("What is the capital of France?: "),
           ("What is the chemical symbol for water?: "),
           ("Which of the following is a Python data type?: "),
           ("Which artist sang the hit song Shape of You?: "),
           ("In which year did World War II end?: "),)

options = (("A) Berlin", "B) Madrid", "C) Paris", "D) Rome"), 
           ( "A) H2O", "B) O2", "C) CO2", "D) NaCl"),
           ( "A) Array", "B) List", "C) Stack", "D) Queue"), 
           ("A) Ed Sheeran", "B) Justin Bieber", "C) Adele", "D) Taylor Swift"), 
           ( "A) 1942", "B) 1945", "C) 1948", "D) 1950"))

answers = ("C", "A", "B", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter an option: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!!")
    else:
        print("INCORRECT!!")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1
print("-------------------------")
print("RESULTS")
print("-------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print() 
print("guesses: ", end="")
for guess in guesses:   
    print(guess, end=" ")       
print()

score = int(score / len(questions) * 100)
print(f"your score is: {score}%")




# #concession stand program 🍿

# menu = {"pizza": 3.00,
#         "burger": 4.60,
#         "fries": 2.00,
#         "coke": 4.00,
#         "chips": 2.20,
#         "popcorn": 3.50,
#         "lemonade": 2.60,
#         "chicken & chips": 5.00,

#         }

# cart = []
# total = 0 
# print("----------MENU-----------")
# for key, value in menu.items():
#     print(f"{key:10} : ${value:.2f}")
# print("-------------------------")


# while True:
#      food = input("Select an item (q to quit): ").lower()
#      if food == "q":
#           break 
#      elif menu.get(food) is not None:
#           cart.append(food)
# print("++++++++++++++YOUR ORDER+++++++++++++++")
# for food in cart:
#      total += menu.get(food)
#      print(food, end =" ")
# print()
# print(f"Total is ${total:.2f}")
      


# #number guessing games
# import random

# lowest_num = 1
# highest_num = 100
# answer = random.randint(lowest_num, highest_num)
# guesses = 0
# is_running = True


# print("Python Number Guessing Game")
# print(f"Select a number between {lowest_num} and {highest_num}")


# while is_running:
#     guess = input("Enter your guess: ")
#     if guess.isdigit():
#         guess = int(guess)
#         guesses += 1
#         if guess < lowest_num or guess > highest_num:
#             print("that number is out of range")
#             print(f"PLEASE select a number between {lowest_num} and {highest_num}")
#         elif guess < answer:
#           print("too low guess higher")  
#         elif guess > answer:
#             print("too high guess lower")
#         else :
#             print(f"CORRECT!!! \n The answer was {answer}")
#             print(f"Number of guesses: {guesses}")
#             is_running = False
#     else:
#         print("invalid guess")
#         print(f"PLEASE select a number between {lowest_num} and {highest_num}")



# rock paper scissor game
# import random
# option =("rock", "paper","scissors")
# win = 0
# lose = 0
# running = True
# while running:
#     player = None
#     computer = random.choice(option)
#     while player not in option:
#         player = input("enter a choice (rock, paper, scissors): ")
#     print(f"Player: {player}")
#     print(f"Computer: {computer}")
#     if player == computer:
#         print("it a tie")
#     elif player == "paper" and computer == "rock":
#         print("you win")
#         win += 1
#     elif player == "rock" and computer == "paper":
#         print("you lose")
#         lose += 1
#     elif player == "scissors" and computer == "rock":
#         print("you lose")
#         lose += 1
#     elif player == "rock" and computer == "scissors":
#         print("you win")
#         win += 1
#     elif player == "paper" and computer == "scissors":
#         print("you lose")
#         lose += 1
#     elif player == "scissors" and computer == "paper":
#         print("you win")
#         win += 1


#     if not input("play again? (y/n): ").lower() == "y":
#             running = False
# print(f"you won {win} times")
# print(f"you lost {lose} times")
# print("Thanks for playing")




#dice game
# import random

# #print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
 
# #● ┌ ─ ┐ │ └ ┘


# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"




# dice_art = {
#     1: ("┌─────────┐",
#         "│         │", 
#         "│    ●    │", 
#         "│         │",
#         "└─────────┘"),

#     2: ("┌─────────┐",
#         "│ ●       │", 
#         "│         │", 
#         "│       ● │",
#         "└─────────┘"),

#     3: ("┌─────────┐",
#         "│ ●       │", 
#         "│    ●    │", 
#         "│       ● │",
#         "└─────────┘"),

#     4: ("┌─────────┐",
#         "│ ●     ● │", 
#         "│         │", 
#         "│ ●     ● │",
#         "└─────────┘"),

#     5: ("┌─────────┐",
#         "│ ●     ● │", 
#         "│    ●    │", 
#         "│ ●     ● │",
#         "└─────────┘"),

#     6: ("┌─────────┐",
#         "│ ●     ● │", 
#         "│ ●     ● │", 
#         "│ ●     ● │",
#         "└─────────┘")
# }
# dice = []
# total = 0
# num_of_dice = int(input("How many dice?: "))

# for die in range(num_of_dice):
#     dice.append(random.randint(1,6))
# for die in range(num_of_dice):
#     for line in dice_art.get(dice[die]):
#         print(line)


# for die in dice:
#     total += die
# print(f"total: {total}")




# #banking program
# def show_balance(balance):
#     print("---------------------------------")
#     print(f"Your balance is ${balance:.2f}")

# def deposit():
#     print("---------------------------------")
#     amount = float(input("Enter amount to be deposited: "))


#     if amount < 0:
#         print("That's not a valid amount")
#         return 0 
#     else:
#         return amount
    
# def withdraw(balance):
#     print("---------------------------------")
#     amount = float(input("Enter amount to be withdrawn: "))
#     if amount > balance:
#         print("Insufficient funds")
#         return 0
#     elif amount < 0:
#         print("Amount must be greater than 0")
#         return 0
#     else:
#         return amount


# def main ():
#     balance = 0
#     is_running = True
   
#     while is_running:
#         print("---------------------------------")
#         print("BANKING PROGRAM")
#         print("1.Show Balance")
#         print("2.Deposit")
#         print("3.Withdraw")
#         print("4.Exit")
#         print("---------------------------------")

#         choice = input("Enter your choice (1-4): ")

#         if choice == "1":
#             show_balance(balance)
#         elif choice == "2":
#             balance += deposit()
#         elif choice == "3":
#             balance -= withdraw(balance)
#         elif choice == "4":
#             is_running = False
            
#         else:
#             print("Invalid choice")


#     print("Thank you have a nice day!!")




# if __name__ == '__main__':
#     main()















# # #python slot machine
# import random
# def spin_row():
#     symbols = ["🍒", "🍉", "🍈", "🔔", "🌟"]
#     # results = []
#     # for symbol in range(3):
#     #     results.append(random.choice(symbols))
#     # return results
#     return [random.choice(symbols) for _ in range(3)]
    

# def print_row(row):
#     print("*************")
#     print(" | ".join(row))
#     print("*************")
# def get_payout(row, bet):
#     if row[0] == row[1] == row[2]:
#         if row[0] == "🍒":
#             return bet * 3
#         elif row[0] == "🍉":
#             return bet *4
#         elif row [0] == "🍈":
#             return bet *5
#         elif row [0] == "🔔":
#             return bet *10
#         elif row [0] == "🌟":
#             return bet *20
#     return 0



# def main():
#     balance = 100
#     print("**********************")
#     print("Welcome to Python Slots")
#     print("Symblos: 🍒 🍉 🍈 🔔 🌟 ")
#     print("***********************")

#     while balance > 0 :
#         print(f"Current balance: ${balance}")

#         bet = input("Place your bet amount: ")

#         if not bet.isdigit():
#             print("Place enter a valid number")
#             continue

#         bet = int(bet)

#         if bet > balance:
#             print("Insuffient funds")
#             continue

#         if bet <= 0:
#             print("Bet must be greater than 0")
#             continue

#         balance -= bet 
#         row = spin_row()
#         print("Spinning...\n")
        
#         print_row(row)

#         payout = get_payout(row, bet)

#         if payout > 0:
#             print(f"You won ${payout}")
#         else:
#             print("sorry you lost")
        
#         balance += payout

#         play_again = input("Do you want to spin again? (Y/N): ").upper()
#         if play_again != "Y":
#             break
#     print("********************************************")
#     print(f"Game over! Your Final balance is ${balance}")
#     print("********************************************")


# if __name__ == '__main__':
#     main()







# # # encryption program 🔐

# # import random
# # import string

# # chars = " " + string.punctuation + string.digits + string.ascii_letters

# # chars = list(chars)
# # key = chars.copy()





# # random.shuffle(key)
# # # print(f"chars: {chars}")
# # # print(f"key: {key}")


# # #ENCRYPT
# # plan_text = input("Enter a message to encrypt: ")
# # cipher_text  = ""

# # for letter in plan_text:
# #     index = chars.index(letter)
# #     cipher_text += key[index]

# # print(f"original message: {plan_text}")
# # print(f"encrypted message: {cipher_text}")


# # #DECRYPT
# # cipher_text  = input("Enter a message to decrypt: ")
# # plan_text  = ""

# # for letter in cipher_text:
# #     index = key.index(letter)
# #     plan_text+= chars[index]

# # print(f"encrypted message: {cipher_text}")
# # print(f"original message: {plan_text}")




# # #hangman game 🕺

# # import random

# # words = ("apple", "orange", "banana", "coconut", "pineapple")
# # #dictionary of key:()
# # hangman_art = {
# #     0: ("   ",
# #         "   ",
# #         "   "),

# #     1: (" o ",
# #         "   ",
# #         "   "),

# #     2: (" o ",
# #         " | ",
# #         "   "),

# #     3: (" o ",
# #         "/| ",
# #         "   "),

# #     4: (" o ",
# #         "/|\\",
# #         "   "),

# #     5: (" o ",
# #         "/|\\",
# #         "/   "),

#     6: (" o ",
#         "/|\\",
#         "/ \\")
# }


# def display_man(wrong_guesses):
#     print("***************")
#     for line in hangman_art[wrong_guesses]:
#         print(line)
#     print("***************")
# def display_hint(hint):
#     print(" ".join(hint))
# def display_answer(answer):
#     print(" ".join(answer))

# def main():
#     answer = random.choice(words)
#     hint = ["_"] * len(answer)
#     wrong_guesses = 0
#     gussed_letters = set()
#     is_running = True


#     while is_running:
#         display_man(wrong_guesses)
#         display_hint(hint)
#         guess = input("Enter a letter: ").lower



# if __name__ == '__main__':
#     main()











# Alarm clock

# import time
# import datetime
# import pygame



# def set_alarm(alarm_time):
#     print(f"Alarm set for {alarm_time}")
#     sound_file = "My_music.mp3"
#     is_running = True

#     while is_running:
#         current_time =  datetime.datetime.now().strftime("%H:%M:%S")
#         print(current_time)
        
#         if current_time == alarm_time:
#             print("Wake up!!")
#             pygame.mixer.init()
#             pygame.mixer.music.load(sound_file)
#             pygame.mixer.music.play()
            
#             while pygame.mixer.music.get_busy():
#                 time.sleep(1)
#             is_running = False
#         time.sleep(1)

# if __name__ == "__main__":
#     alarm_time = input("Enter the alarm time(HH:MM:SS): ")
#     set_alarm(alarm_time)

