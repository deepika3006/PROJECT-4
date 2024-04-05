import random
import string

def generate_password(length):
    # Define characters to use in password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate password using random.choice for each character
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    # User input for password length
    length = int(input("Enter the length of the password: "))
    # Generate and print password
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
