import argparse
import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    if not any([use_uppercase, use_lowercase, use_digits, use_special]):
        raise ValueError("At least one character type must be selected")

    char_pool = ""
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_lowercase:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_special:
        char_pool += string.punctuation

    if len(char_pool) == 0:
        raise ValueError("Character pool is empty. Enable at least one character type.")

    # Ensure that the length is a positive integer
    if length <= 0:
        raise ValueError("Length must be a positive integer")

    # Generate password using random.choices to allow repetitions and ensure length
    password = ''.join(random.choices(char_pool, k=length))
    return password

def main():
    parser = argparse.ArgumentParser(description="Generate a random password with customizable complexity.")
    parser.add_argument('--length', type=int, required=True, help='Length of the password')
    parser.add_argument('--uppercase', action='store_true', help='Include uppercase letters')
    parser.add_argument('--lowercase', action='store_true', help='Include lowercase letters')
    parser.add_argument('--digits', action='store_true', help='Include digits')
    parser.add_argument('--special', action='store_true', help='Include special characters')

    args = parser.parse_args()

    try:
        password = generate_password(args.length, args.uppercase, args.lowercase, args.digits, args.special)
        print(f"The Requested Password is:~ {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
