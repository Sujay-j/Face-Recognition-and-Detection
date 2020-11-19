from tkinter import *
import os
import time


def main():
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Login")
    screen.configure(background = 'turquoise')
    Button(screen,text="Login",height = "2",width ="20",fg='white',bg='purple',font=('comicsans',12),command = login).place(x=70,y=100)
    Label(screen,text="WELCOME TO FACIAL RECONIZATION ",fg='purple',bg='turquoise',font=('comicsans',10)).pack()
    screen.mainloop()

def login():
    os.system('python faces-train.py')
    time.sleep(5)
    print("training data")
    os.system('python faces.py')
    
    


main()
