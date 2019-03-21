import hashlib  # Generate md5 sum for pass
import base64  # Imports base64 library


def ssymbols(npass):
    npass = npass.replace('A', '@')
    npass = npass.replace('a', '@')
    npass = npass.replace('C', '`')
    npass = npass.replace('c', '`')
    npass = npass.replace('E', '-')
    npass = npass.replace('e', '-')
    npass = npass.replace('G', '+')
    npass = npass.replace('g', '+')
    npass = npass.replace('I', '|')
    npass = npass.replace('i', '|')
    npass = npass.replace('K', '.')
    npass = npass.replace('k', '.')
    npass = npass.replace('L', '!')
    npass = npass.replace('l', '!')
    npass = npass.replace('N', '#')
    npass = npass.replace('n', '#')
    npass = npass.replace('O', ',')
    npass = npass.replace('o', ',')
    npass = npass.replace('S', '$')
    npass = npass.replace('s', '$')
    npass = npass.replace('U', '*')
    npass = npass.replace('u', '*')
    return npass


def gen(ent_passphrase, ent_passlength):
    pl = int(ent_passlength)  # Makes an integer
    passlength = pl
    yourpass = str(ent_passphrase)
    # print(yourpass) # TEST
    yourpass = yourpass.title().strip()  # Make every word with Upper first letter and delete spaces at boards
    # print("------\n\n" + yourpass + "\n\n------") # TEST
    yourpass = hashlib.md5(yourpass.encode()).hexdigest()  # Generates md5 checksum
    yourpass = str(yourpass * 2).encode()
    # print("------\n\n" + yourpass + "\n\n------") # TEST
    yourpass = base64.b64encode(bytes(yourpass))  # Generate md5 checksum
    yourpass = str(yourpass * 2).encode()
    # print("------\n\n" + yourpass + "\n\n------") # TEST
    yourpass = base64.b64encode(bytes(yourpass))  # Generate md5 checksum
    yourpass = str(yourpass)
    passlength = int(passlength)
    n = 80 + passlength
    start = n // 9
    npass = yourpass[start:start + passlength]  # Cut from X symbol of string
    npass = str(npass)
    return npass


def main():
    welcome = "Hello! This programm will help you to generate your password."
    description = "You should just input the length of your password and phrase that your password will be based on."
    text_pass_phrase = "Please, enter your password phrase:"
    text_password_length = "What length of password you want (number of symbols)?"
    password_notification = "Your password is: "
    text_ssymbols = "Are you want to use special symbols? [y/n]"

    print(welcome)
    print(description)
    print(text_pass_phrase)
    pass_phrase = input()
    print(text_password_length)
    pass_length = input()
    print(text_ssymbols)
    ssymbols = input()
    password = gen(pass_phrase, pass_length)
    if ssymbols == "y":
        password = ssymbols(password)
    print(password_notification + password)


if __name__ == "__main__":
    main()
