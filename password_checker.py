import re

def check_password_strength(password):
   
    # First checking the minimum length of password
    if len(password) < 8:
        return False

    # Then we will check for at least one uppercase and one lowercase letter
    if not (any(c.isupper() for c in password) and any(c.islower() for c in password)):
        return False

    # After that we need to check for at least one digit
    if not any(c.isdigit() for c in password):
        return False

    # Then we have to check for at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False

    # If all the criteria is passed, then the password is strong
    return True

def main():

    # For taking user input for password
    password = input("Enter your password: ")

    # Strength checking of the password
    if check_password_strength(password):
        print("✅ Your password is strong! It meets all the criteria.")
    else:
        print("❌ Your password is weak. Please ensure it meets the following criteria:")
        print("- At least 8 characters long")
        print("- Contains both uppercase and lowercase letters")
        print("- Contains at least one digit (0-9)")
        print("- Contains at least one special character (e.g., !, @, #, $, %)")

if __name__ == "__main__":
    main()