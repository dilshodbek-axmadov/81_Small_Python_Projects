import string

alphabet = string.ascii_lowercase

user_input = input("Enter the encrypted Ceaser cipher message to hack.\n> ")
actual_text = []
for i in range(len(alphabet)):
    actual_text.append("")
    for char in user_input:
        if char.lower() in alphabet:
            index = alphabet.index(char.lower())
            new_index = index-i
            new_char = alphabet[new_index%len(alphabet)]

            if char.isupper():
                actual_text[i] += new_char.upper()
            else:
                actual_text[i] += new_char
        else:
            actual_text[i]+=char
for shift_key, decrypted_message in enumerate(actual_text):
    print(f"Key #{shift_key}: {decrypted_message}")