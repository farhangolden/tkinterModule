from tkinter import *
from tkinter import messagebox

def greeting():
    messagebox.showinfo("Greeting","Good Morning!"+username.get())

window=Tk()
window.title("First GUI application")
# window.geometry("600x400")
window.resizable(True,True)
username=StringVar()
L1=Label(text="First GUI applicaton",font=("Arial",20,"bold"))
L1.pack()
L2=Label(text="Enter User Name",font=("Arial",16,"bold"))
L2.pack()
E1=Entry(font=("Arial",16,"normal"),textvariable=username)
E1.pack()
B1=Button(text=("Click Here!"),font=("Arial",16,"normal"),command=greeting)
B1.pack()

window=mainloop()