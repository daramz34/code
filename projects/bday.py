import datetime

name = input("Enter name: ").upper()
today = datetime.date.today().strftime('%m-%d')

# ASCII-style banner for "HAPPY BIRTHDAY"

Banner = [
    " ██     ██    █████    ███████   ███████    ██        ██        ███████    ████████    ████████    ████████      ██     ██      ██████        ██████     ██          ██",
    " ██     ██   ██   ██   ██    ██  ██    ██    ██      ██         ██   ██       ██       ██   ███       ██         ██     ██      ██   ██      ██    ██      ██       ██",
    " ██     ██   ███████   ██████    ██████        ██   ██          ██  ██        ██       ██  ██         ██         █████████      ██    ██     ██    ██        ██   ██",
    " █████████   ██   ██   ██        ██              ███            ██  ██        ██       ████           ██         ██     ██      ██    ██     ████████          ███",
    " ██     ██   ██   ██   ██        ██              ███            ██   ██       ██       ██  ██         ██         ██     ██      ██   ██      ██    ██          ███",
    " ██     ██   ██   ██   ██        ██              ███            ██ ██       ███████    ██    ██       ██         ██     ██      █████        ██    ██          ███"
    
]

print(f"\nToday: {today} - Birthday vibes! 🎈\n")
for line in Banner:
    print(line)
print(f"\n{name}!\n🥂 Wishing you a joyful, unforgettable birthday!")



# import datetime

# # Ask for the person's name and birthday
# name = input("What's your name? ")
# birth_date = input("Enter your birthday (YYYY-MM-DD): ")

# # Convert input to a date object
# birth_date = datetime.datetime.strptime(birth_date, "%Y-%m-%d").date()
# today = datetime.date.today()

# # Check if today is their birthday
# if birth_date.month == today.month and birth_date.day == today.day:
#     print(f"\n🎉 Happy Birthday, {name}! 🎂")
#     print("Wishing you joy, laughter, and cake today!")
# else:
#     print(f"\nHi {name}, your birthday is on {birth_date.strftime('%B %d')}.")
#     print("I'll be ready to celebrate when the day comes! 🎈")









       
# import datetime

# # Get user's name and birthday
# name = input("Enter your name: ").capitalize()
# birth_input = input("Enter your birthday (MM-DD): ")

# # Get today's date
# today = datetime.date.today()
# current_year = today.year

# # Convert birthday to a date object
# birth_month, birth_day = map(int, birth_input.split('-'))
# birthday = datetime.date(current_year, birth_month, birth_day)

# # If birthday has passed this year, use next year
# if birthday < today:
#     birthday = datetime.date(current_year + 1, birth_month, birth_day)

# # Calculate days left
# days_left = (birthday - today).days

# # Output
# print("\n🎉 Birthday Countdown 🎉")
# if days_left == 0:
#     print(f"\n🎂 Happy Birthday, {name}!!! 🎊🎈")
#     print("Wishing you love, laughter, and lots of cake today!")
# else:
#     print(f"\nHi {name}, your birthday is in {days_left} day(s) 🎁")
#     print("Hang in there — the celebration is coming!")









# name = input("Enter name: ").upper()
# style = input("Choose banner style (stars/hearts/emojis): ").lower()

# if style == "stars":
#     symbol = "*"
# elif style == "hearts":
#     symbol = "❤"
# else:
#     symbol = "🎉"

# print(f"\n{symbol * 10} HAPPY BIRTHDAY {name} {symbol * 10}")



# name = input("Enter recipient's name: ").title()
# message = f"Happy Birthday, {name}! 🎂\nWishing you joy, love, and laughter today!"

# border = "❤" * (len(message) + 4)
# print("\n" + border)
# print(f"* {message} *")
# print(border)
