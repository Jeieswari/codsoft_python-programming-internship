import random
import string

def generate_password(length, complexity):
    
    if complexity == 'basic':
        characters = string.ascii_lowercase  
    elif complexity == 'medium':
        characters = string.ascii_letters  
    elif complexity == 'strong':
        characters = string.ascii_letters + string.digits + string.punctuation  
    else:
        print("Invalid complexity level. Defaulting to 'strong'.")
        characters = string.ascii_letters + string.digits + string.punctuation

    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 6:
                print("Password length should be at least 6 characters.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for the length.")
    
    
    complexity = input("Choose the complexity (basic, medium, strong): ").lower()

    
    password = generate_password(length, complexity)
    print(f"Generated password: {password}")


main()
