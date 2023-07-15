import random
import string

program_name = '''
 _____               _____
|  __ \             / ____|
| |__) |_ _ ___ ___| |  __  ___ _ __
|  ___/ _` / __/ __| | |_ |/ _ \ '_  \\
| |  | (_| \__ \__ \ |__| |  __/ | | |
|_|   \__,_|___/___/\_____|\___|_| |_|
'''

def get_valid_input(message, valid_options):
    while True:
        user_input = input(message).lower()
        if user_input in valid_options:
            return user_input
        print("Invalid input. Please enter a valid option")

def generate_password():
    print("Welcome to", program_name)
    print("\nProject Name: Random Password Generator in Python")
    print("Intern Name: Rethar Osman Abdullah")
    print("Intern ID: CC36307")
    print("Designation: Python Development Intern\n")
    while True:
        try:
            length = int(input("\nEnter desired password length: "))  # Prompt the user to enter the desired password length as an integer
            if length <= 0:
                print("\nPassword length must be a positive number.")  # Display an error message if the length is not positive
                continue

            use_uppercase = get_valid_input("\nInclude uppercase letters? (y/n): ", ["y", "n"]) == "y"  # Prompt the user to include uppercase letters
            use_special_characters = get_valid_input("\nInclude special characters? (y/n): ", ["y", "n"]) == "y"  # Prompt the user to include special characters
            use_numbers = get_valid_input("\nInclude numbers? (y/n): ", ["y", "n"]) == "y"  # Prompt the user to include number integers

            characters = string.ascii_lowercase  # Set the characters variable with lowercase letters

            if use_uppercase:
                characters += string.ascii_uppercase  # Append uppercase letters to the characters variable if the user wants them included
            if use_special_characters:
                characters += string.punctuation  # Append special characters to the characters variable if the user wants them included
            if use_numbers:
                characters += string.digits  # Append number integers to the characters variable if the user wants them included

            password = "".join(random.choice(characters) for _ in range(length))  # Generate the password using random.choice and list comprehension
            print("\nGenerated Password:", password)

            exit_program = get_valid_input("\nDo you want to exit the program? (y/n): ", ["y", "n"])  # Prompt the user to either exit or continue
            if exit_program == "y":
                print("\nThank you for using PassGen, my Password Generator")
                break

        except ValueError:
            print("\nInvalid input. Please enter a valid number for the password length")  # Display an error message if the entered value is not a valid integer

generate_password()
