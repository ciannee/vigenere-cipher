# Name: Pineda, Patricia Anne E.
# Section: BSCPE 1-5
# Assignment 3 : Redo Problem 3 with multiple github commits (Vigenere Cipher)

# looping
cipher_str = ""
while cipher_str != "no":

# build class of colors to print color text
    class colors:
    
        reset = '\033[0m'
        bold = '\033[01m'
        disable = '\033[02m'
        underline = '\033[04m'
        reverse = '\033[07m'
        strikethrough = '\033[09m'
        invisible = '\033[08m'

    class fg:

        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'

    #ask for user's input
    name = input("\n\033[01mPlease enter your name: ")
    kawaii = ("₍ ᐢ.ˬ.ᐢ₎")
    import time
    time.sleep(3)

    import pyfiglet
    name_art = pyfiglet.figlet_format(name, font='banner3-D')

    kawaii = ("₍ ᐢ.ˬ.ᐢ₎")
    
    #print output
    print("Hi.......\n\n\n" + colors.underline, name_art)
    print("\n\n ══✿══╡°˖ This is the Vigenere Cipher! ✧˖°╞══✿══")

    # convert letter to index and index to letter
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    letter_to_index = dict(zip(alphabet, range(len(alphabet))))
    index_to_letter = dict(zip(range(len(alphabet)), alphabet))

    def encrypt (message, key):
        encrypted = ""

        # split the message to the length of the key
        split_message = [message[i:i + len(key)] for i in range (0, len(message), len(key))] # start, end, step
        
        # convert message to index and add key
        for each_split in split_message:
            i = 0
            for letter in each_split:
                number = (letter_to_index[letter] + letter_to_index[key[i]]) % len(alphabet)
                encrypted += index_to_letter[number]
                i += 1
        
        return encrypted 


    def decrypt (cipher, key):
        decrypted = ""

        # split ciphertext to the length of key
        split_cipher = [cipher[i:i + len(key)] for i in range(0, len(cipher), len(key))] # start, end, step

        # convert ciphertext to index and subtract key 
        for each_split in split_cipher:
            i = 0
            for letter in each_split:
                number = (letter_to_index[letter] - letter_to_index[key[i]]) % len(alphabet)
                decrypted += index_to_letter[number]
                i += 1
        
        return decrypted

    def main ():
        key = "knights"
        message = "thisisthelasttaskhoorday"
        encrypted_message = encrypt(message, key)

        import time
        time.sleep(3)
        print("\n  █▒▒▒▒▒▒▒▒▒")
        time.sleep(1)
        print("\n  ███▒▒▒▒▒▒▒")
        time.sleep(1)
        print("\n  █████▒▒▒▒▒")
        time.sleep(1)
        print("\n  ███████▒▒▒")
        time.sleep(1)
        print("\n  ██████████")

        print("\n\033[33m• • • • • • • The Message is: • • • • • • • " + "\n\n\t" + message.upper())
        time.sleep(3)
        print("\n\033[93m• • • • • • • The Ciphertext will be: • • • • • • • " + "\n\n\t" + encrypted_message.upper())
    
    main()

    # looping
    time.sleep(3)
    cipher_str = input("\n\n\033[35mDo you want to try the Vigenere Cipher again? \n\nPlease enter YES or NO: ")
    if cipher_str == "YES":
        # print outro