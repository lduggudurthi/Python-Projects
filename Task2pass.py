
import random
import string

def generate_password(length):
    # Define the character sets for different complexities
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    # Combine all character sets based on complexity
    all_characters = lower_case + upper_case + digits + punctuation

    # Generate password using random choices
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    try:
        # Prompt user for password length
        length = int(input("Enter the desired length of the password: "))

        if length <= 0:
            print("Length must be a positive integer.")
            return

        # Generate password
        password = generate_password(length)

        # Display generated password
        print("Generated Password:", password)

    except ValueError:
        print("Invalid input. Please enter a valid integer for the length.")

if __name__ == "__main__":
    main()
