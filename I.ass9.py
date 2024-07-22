import random
import string

def generate_password(length=12):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Take user input for the length of the password
try:
    length = int(input("Enter the length of the password (default is 12): "))
    if length <= 0:
        raise ValueError("Length must be a positive integer.")
except ValueError as e:
    print(f"Invalid input: {e}. Using default password length of 12.")
    length = 12

# Generate and print the password
random_password = generate_password(length)
print(f"Generated Password: {random_password}")