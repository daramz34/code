import sys


def add_task():
    task = input("Enter task: ")

    with open("tutoralhell\\tasks.txt", "a") as file:
        file.writelines(f"\n [ ] {task}")
    print("Task added")

def marked_task():
    tasks = []
    id = int(input("Enter task you want to mark done: "))
                
    with open("tutoralhell\\tasks.txt", "r") as file:
        lines = file.readlines()

        if id < 1 or id >= len(lines):
            print("Invalid task number")
            return
        
        lines[id] =lines[id].replace("[ ]", "[x]")
        with open("tutoralhell\\tasks.txt", "w") as file:
            file.writelines(lines)
            print("***** Marked done ******")
               
         
    #
    #if id in tasks:
    #         print("**** Marked tasked ****")
    #         print(f"\n [x] {i,v}")
    # else:
    #         print("yyyyyy")


def view_task():
     with open("tutoralhell\\tasks.txt", "r") as file:
        for i, v in enumerate(file, 0):
            if i != 0:
                print(i,v)
        


while True:
    print("\n === Welcome to the to do list app ===")
    print("1. Add task")
    print("2. View all task")
    print("3. Mark task you have done")
    print("4. Exit")
    choice = input("Choose an option: ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3": 
        marked_task()
    elif choice == "4":
        print("Goodbye👋")
        break

