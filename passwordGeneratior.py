import string
import random

if __name__ == "__main__":
    try:
        length = int(input("Enter the length of the password: "))
        
        # Validate length
        if length < 4:
            print("Password too short! Using length 8")
            length = 8
        elif length > 94:
            print("Password too long! Maximum is 94. Using 94")
            length = 94
        
        letters = string.ascii_letters
        digits = string.digits
        punctuation = string.punctuation
        all_characters = letters + digits + punctuation
        password = "".join(random.sample(all_characters, length))
        print("Generated password:", password)
        
    except ValueError:
        print("Error: Please enter a valid number!")