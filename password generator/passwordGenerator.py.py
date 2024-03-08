#i am tushar sharma i made this mini project for it external classes or exam
import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars):
    chars = ""
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_numbers:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation

    if not any([use_uppercase, use_lowercase, use_numbers, use_special_chars]):
        print("Please select at least one character type.")
        return None

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    length = int(input("Enter the length of the password: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars)
    if password:
        print("Generated Password:", password)

if _name_ == "_main_":
    main()