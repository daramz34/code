# s = "Geeks for Geeks"
# word = "Geeks"

# b = s.split(" ")
# print(b)
# for i in b: 
#     if (i == word):
#      print("bbbb")









# # def word_in_file(filename, word):
# #     try:
# #         # Open file in read mode with UTF-8 encoding
# #         with open(filename, 'r', encoding='utf-8') as file:
# #             content = file.read()

# #         # Case-insensitive search
# #         return word.lower() in content.lower()

# #     except FileNotFoundError:
# #         print(f"Error: File '{filename}' not found.")
# #         return False
# #     except Exception as e:
# #         print(f"An error occurred: {e}")
# #         return False


# # # Example usage
# # if __name__ == "__main__":
# #     file_path = "example.txt"  # Replace with your file path
# #     search_word = "Python"     # Replace with the word you want to search

# #     if word_in_file(file_path, search_word):
# #         print(f"'{search_word}' was found in '{file_path}'.")
# #     else:
# #         print(f"'{search_word}' was NOT found in '{file_path}'.")















# txt = "Hello, welcome to my world"
# x = txt.find("welcome")

# print(x)





# from datetime import datetime, date, time, timedelta

# # 1. Get the current date and time
# now = datetime.now()
# print("Current datetime:", now)


# formatted = now.strftime("%Y-%m-%d %H:%M:%S")
# print("Formatted datetime:", formatted)


# import os
# directory_name = "GfG"

# try:
#     os.mkdir(directory_name)
#     print(f"Directory {directory_name} created successfully.")
# except FileExistsError:
#     print("bbb")



# import library
import math, random

# function to generate OTP
def generateOTP() :

    # Declare a string variable  
    # which stores all string 
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    OTP = ""
    length = len(string)
    for i in range(6) :
        OTP += string[math.floor(random.random() * length)]

    return OTP

# Driver code
if __name__ == "__main__" :
    
    print("OTP of length 6:", generateOTP())