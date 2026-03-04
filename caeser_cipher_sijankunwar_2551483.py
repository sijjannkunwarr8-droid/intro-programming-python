import os

def welcome():
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text using the Caesar Cipher.")

def enter_message(mode):
    if mode == 'e':
        message = input("What message would you like to encrypt: ").upper()
    else:
        message = input("What message would you like to decrypt: ").upper()
    return message

def encrypt(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            result += chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            result += char
    return result

def decrypt(message, shift):
    return encrypt(message, -shift)

def process_file(filename, mode, shift):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    result = []
    for line in lines:
        line = line.strip().upper()
        if mode == 'e':
            result.append(encrypt(line, shift))
        else:
            result.append(decrypt(line, shift))
    
    return result

def is_file(filename):
    return os.path.isfile(filename)

def write_messages(messages):
    with open('results.txt', 'w') as file:
        for message in messages:
            file.write(message + "\n")

def message_or_file():
    while True:
        source = input("Would you like to read from a file (f) or the console (c)? ").lower()
        if source in ['f', 'c']:
            break
        else:
            print("Invalid Source")
    
    if source == 'c':
        return None  # No filename
    else:
        while True:
            filename = input("Enter a filename: ")
            if is_file(filename):
                break
            else:
                print("Invalid Filename! Please enter a valid file name")
        
        return filename

def main():
    welcome()
    while True:
        while True:
            mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
            if mode in ['e', 'd']:
                break
            else:
                print("Invalid Mode")

        filename = message_or_file()
        
        while True:
            try:
                shift = int(input("What is the shift number: "))
                break
            except ValueError:
                print("Invalid Shift Number")

        if filename:
            result = process_file(filename, mode, shift)
            write_messages(result)
            print("Output written to results.txt")
        else:
            message = enter_message(mode)
            if mode == 'e':
                result = encrypt(message, shift)
            else:
                result = decrypt(message, shift)
            print(result)
        
        while True:
            retry = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
            if retry in ['y', 'n']:
                break
            else:
                print("Invalid Response")
        
        if retry == 'n':
            print("Thanks for using the program, goodbye!")
            break

main()
