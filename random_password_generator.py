from tkinter import *
import pyperclip as pc

import random
root=Tk()
root.geometry("450x350")
passwstr= StringVar()
passlen= IntVar()
passlen.set(0)

def generator():
    pass1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
           'q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6',
           '7','8','9','0','_','!','@','#','$','%','^','&','*','(',')']
    password=""
    for i in range(passlen.get()):
        password=password+ random.choice(pass1)
    passwstr.set(password)
def copyclipboard():
    random_password=passwstr.get()
    pc.copy(random_password)

Label(root,text="Password Generator Application",font="calibri 20 bold").pack()

Label(root,text="Enter Password length").pack(pady=3)
Entry(root,textvariable=passlen).pack(pady=3)

Button(root,text="Generate Password",command=generator).pack(pady=7)

Entry(root,textvariable=passwstr).pack(pady=3)

Button(root,text="Copy clipboard",command=copyclipboard).pack()

root.mainloop()