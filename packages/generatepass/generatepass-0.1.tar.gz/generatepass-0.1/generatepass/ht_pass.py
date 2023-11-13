#password generator::
#Hizart soft::harsdev corp H._T @2022

from getpass import getpass
import random
import string

def generate_pass(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_pass(password):
    length_criteria = 8
    uppercase_criteria = 1
    digit_criteria = 1
    special_char_criteria = 1

    if len(password) < length_criteria:
        return 'Low: Password is too short.'

    if sum(1 for char in password if char.isupper()) < uppercase_criteria:
        return 'Low: Include at least {} uppercase letter(s).'.format(uppercase_criteria)

    if sum(1 for char in password if char.isdigit()) < digit_criteria:
        return 'Low: Include at least {} digit(s).'.format(digit_criteria)

    if sum(1 for char in password if char in string.punctuation) < special_char_criteria:
        return 'Low: Include at least {} special character(s).'.format(special_char_criteria)

    return 'Normal: Password meets the criteria.'

def use_encrypt_pass(password):
    encrypted_password = ''.join(chr(ord(char) + 1) for char in password)
    return encrypted_password

def use_decrypt_pass(encrypted_password):
    decrypted_password = ''.join(chr(ord(char) - 1) for char in encrypted_password)
    return decrypted_password

def get_user_password():
    # Use getpass to securely input the password
    user_password = getpass("Enter your password: ")
    return user_password




