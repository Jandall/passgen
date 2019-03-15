import hashlib  # Generate md5 sum for pass
import base64  # Imports base64 library
import pyperclip  # Module for work with clipboard
from tkinter import *  # Import GUI library


def ssymbols():
    # Replaces symbols below FOR FUTURE FEATURES
    # print('1') # TEST
    global npass
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


def generate(event):
    global count  # This counter uses for better display of buttons (At first displays strings, after just configures those strings
    if count == 0:
        str1.pack()
        str2.pack()
    gen()
    count = count + 1


def gen():
    global yourpass
    global passlength
    global npass
    global start
    global ch1

    # print(ch1.get()) # TEST
    pl = ent_passlength.get()  # Gets a string from a label
    pl = int(pl)  # Makes an integer
    passlength = pl
    yourpass = ent_passphrase.get()
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
    # print("------\n\n" + yourpass + "\n\n------") # TEST
    ypass.configure(textvariable=yourpass, text=yourpass)
    passlength = int(passlength)
    n = 80 + passlength
    start = n // 9
    npass = yourpass[start:start + passlength]  # Cut from X symbol of string
    npass = str(npass)
    if ch1.get() == 1:
        # print('2')  #TEST
        ssymbols()
    str1.configure(text="Your password is:", font=vfont)
    str2.configure(text=npass)
    but_clip.pack()
    but_exit.pack()


def term(event):
    window.destroy()


def clipboard(event):
    pyperclip.copy(npass)  # It copy your fresh-generated password to clipboard


vfont = 'Arial 12'

window = Tk()

line1 = Label(window, text="Hello! This programm will help you to generate your password.", font=vfont)
line2 = Label(window,
              text="You just input the length of your password and phrase \n that your password will be based on.",
              font=vfont)
line3 = Label(window, text="What length of password you want (number of symbols)?", font=vfont)
str1 = Label(window, text="", font=vfont)
str2 = Label(window, text="", font=vfont)

pllabel = Label(window, text="Please, enter your password phrase:", font=vfont)
ypass = Label(window, textvariable="", font=vfont)
npasslabel = Label(window, text="", font=vfont)
ch1 = IntVar()  # Integer variable for checkbutton
count = int(0)  # Counter of generate button

chkbt1 = Checkbutton(window, text="Use special symbols", variable=ch1, onvalue=1, font=vfont)

ent_passlength = Entry(window, width=20, bd=3)  # Field to entry password length
ent_passphrase = Entry(window, width=20, bd=3)  # Field to entry password phrase
ent_passphrase.bind("<Return>", generate)

but_generate = Button(window, text="Generate password", font=vfont)
but_generate.bind("<Button-1>", generate)
but_generate.bind("<Return>", generate)
but_generate.bind("<space>", generate)

but_clip = Button(window, text="Copy password to clipboard", font=vfont)
but_clip.bind("<Button-1>", clipboard)
but_clip.bind("<Return>", clipboard)
but_clip.bind("<space>", clipboard)

but_exit = Button(window, text="Exit program", font=vfont)
but_exit.bind("<Button-1>", term)
but_exit.bind("<Return>", term)
but_exit.bind("<space>", term)

line1.pack()
line2.pack()
line3.pack()
ent_passlength.pack()
pllabel.pack()
ent_passphrase.pack()
chkbt1.pack()
but_generate.pack()

window.mainloop()