import random
import string

def generate_password(length=12):
    # Define character sets for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

if __name__ == "__main__":
    print("Random Password Generator")
    password_length = int(input("Enter the desired password length: "))

    if password_length < 1:
        print("Password length should be at least 1 character.")
    else:
        password = generate_password(password_length)
        print(f"Generated Password: {password}")
