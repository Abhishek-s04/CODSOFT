import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password
try:
    length = int(input("Enter the desired password length: "))
    if length < 1:
        print("Password length must be at least 1.")
    else:
        # Generate the password and display it
        generated_password = generate_password(length)
        print(f"Generated Password: {generated_password}")
except ValueError:
    print("Please enter a valid number for password length.")
