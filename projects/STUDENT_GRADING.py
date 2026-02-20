users = {}
while True:
    print("WELCOME! CHOOSE AN OPTION")
    print("1. REGISTER")
    print("2. LOGIN")
    print("3. EXIT")
    option = input("enter an option: ")
    
    if option == "1":
        while True:
            username = input("ENTER A USERNAME: ")
            if len(username) > 12 :
                print("USERNAME CAN'T BE MORE THAN 12 CHARACTERS")
                continue
            if " " in username: 
                print("USERNAME CAN'T CONTAIN SPACES")
                continue
            if not username.isalpha():
                print("USERNAME CAN'T CONTAIN NUMBERS")
                continue
            break
        while True:
            password = input("ENTER A PASSWORD: ")
            if len(password) < 6:
                print("PASSWORD MUST BE AT LEAST 6 CHARACTERS")
                continue
            if not any(c.isalpha() for c in password):
                print("PASSWORD MUST CONTAIN AT LEAST 1 LETTER")
                continue
            if not any(c.isdigit() for c in password):
                print("PASSWORD MUST CONTAIN AT LEAST 1 NUMBER")
                continue
            break
        users[username] = password
        print(f"WELCOME {username} REGISTRATION SUCCESSFUL")
    elif option == 2:
         username = input("ENTER YOUR USERNAME: ")
         password = input("ENTER YOUR PASSWORD: ")
         if username in users and users[username] == password:
            print(f"Login successful! Welcome back, {username}.")
    else:
            print("invalid login details")


    break
    