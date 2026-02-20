from script1 import *

def favorite_drink(drink):
    print(f"your fav drink is {drink}")
def main():
    print("this is script 2")
    favorite_food("bread")
    favorite_drink("tea")

if __name__ == '__main__':
    main()