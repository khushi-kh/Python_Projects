from art import *

MORSE = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
         'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
         's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',

         '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
         '9': '----.', '0': '-----',

         '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '"': '.-..-.', ':': '---...', ';': '-.-.-.',
         '+': '.-.-.', '-': '-....-', '*': '-..-', '/': '-..-.', '!': '-.-.--', '(': '-.--.', ')': '-.--.-',
         '&': '.-...', '=': '-...-', '_': '..--.-', '$': '...-..-', '@': '.--.-.', ' ': '/'}


def encrypt(message):
    encrypted = ''
    for letter in message:
        encrypted += MORSE[letter.lower()]
        encrypted += " "
    return encrypted


def decrypt(message):
    msg = message.split(' ')
    decrypted = ''
    for word in msg:
        if word in MORSE.values():
            for key, value in MORSE.items():
                if value == word:
                    decrypted += key
        else:
            decrypted += ' '
    return decrypted


def main():
    print(heading)
    print(subheading)
    print("WELCOME TO THE MORSE-CODE TRANSLATOR")
    game_on = True

    while game_on:
        activity = input("Do you want to ENCRYPT or DECRYPT? (Type EXIT to quit the program)\n").lower()

        if activity == 'encrypt':
            print(encryption)
            msg = input("Type the message you want to encrypt to morse code.\n")
            print('Your message in morse code: ', encrypt(msg))

        elif activity == 'decrypt':
            print(decryption)
            msg = input('Type the message you want to decrypt from morse code.\n')
            print('Your message: ', decrypt(msg))

        elif activity == 'exit':
            game_on = False

        else:
            print("INVALID RESPONSE, Please Try again!!!")


if __name__ == '__main__':
    main()
