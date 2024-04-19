import random
import string

def generate_password(length=8):
    
    characters = string.ascii_letters + string.digits + string.punctuation

    
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

if __name__ == "__main__":
    
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            print("Password length must be a positive integer.")
        else:
            generated_password = generate_password(length)
            print("Generated Password:", generated_password)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the password length.")
