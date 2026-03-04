import sys
import random
import string


def generate_password(length): 
    chars = string.ascii_letters + string.digits + string.punctuation
    

    password = ""

    for _ in range(length):
        password += random.choice(chars)
    
    return f"Password: {password}"



if len(sys.argv) > 1:
    length = int(sys.argv[1])
    print(generate_password(length))
else:
    print("Usage: Python password.py <length>")

