import string

alphabet = string.ascii_uppercase

def get_user_key():
    while True:
        user_input = input("Please enter the key (0 to 25) to use.\n> ")
        if not user_input.isdecimal():
            continue
        key = int(user_input)
        if 0 <= key <= 25:
            return key

def cipher(message, key):
    """Positive key = encrypt, negative key = decrypt."""
    new_message = ''
    for char in message:
        if char.upper() in alphabet:
            index = alphabet.index(char.upper())
            new_char = alphabet[(index + key) % len(alphabet)]
            new_message += new_char.lower() if char.islower() else new_char
        else:
            new_message += char
    return new_message


while True:
    user_input = input("Do you want to (e)ncrypt or (d)ecrypt? or (q)uit\n> ").lower()
    if user_input in ('q', 'quit'):
        break
    elif user_input == 'e':
        key = get_user_key()
        message = input("Please enter the message to encrypt\n> ")
        print(cipher(message, key))
    elif user_input == 'd':
        key = get_user_key()
        message = input("Please enter the message to decrypt\n> ")
        print(cipher(message, -key))