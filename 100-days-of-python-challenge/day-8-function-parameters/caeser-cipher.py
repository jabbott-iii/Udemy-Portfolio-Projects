print("Welcome to the Caesar Cipher Encoder!")

alphabet = 'abcdefghijklmnopqrstuvwxyz'
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
shift = int(input("Type the shift number: "))
text = input("Type your message: ").lower()

def encrypt(plain_text, shift_amount):
    encrypted_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % 26
            encrypted_text += alphabet[new_position]
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(cipher_text, shift_amount):
    decrypted_text = ""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_amount) % 26
            decrypted_text += alphabet[new_position]
        else:
            decrypted_text += char
    return decrypted_text

def caesar_cipher(text, shift, direction):
    if direction == "encode":
        return encrypt(text, shift)
    elif direction == "decode":
        return decrypt(text, shift)
    else:
        return "Invalid direction! Please choose 'encode' or 'decode'."

print(caesar_cipher(text, shift, direction))# Caesar Cipher
# This program encodes and decodes messages using the Caesar cipher technique.