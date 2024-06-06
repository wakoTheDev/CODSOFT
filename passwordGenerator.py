import random

def password_generator(password_length, quality):
    if password_length < 4:
        return "Password too short"

    choice_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    alpha_list = list(choice_list)
    symbols = ['~', '!', '@', '#', '$', '%', '^', '&', '*', ':', ';']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    if quality == 'Strong':
        lists = [alpha_list, symbols, numbers]
    elif quality == 'Medium':
        lists = [alpha_list, numbers]
    elif quality == 'Weak':
        lists = [numbers]
    else:
        return "Invalid quality choice"

    password = [random.choice(random.choice(lists)) for _ in range(password_length)]

    return ''.join(password)  # Return the password as a string

password_length = int(input('Enter password length: '))
quality = input('Choose password Quality: Weak, Medium or Strong: ')

print(password_generator(password_length, quality))
