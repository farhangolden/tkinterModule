from tkinter import *
from tkinter import messagebox

def login_Function():
    if user.get()=="" or password.get()=="":
        messagebox.showerror("Blank Input","Please enter your username anfd password!")
    elif user.get()=="Ali" and password.get()=="123.123":
        messagebox.showinfo("Login Succesful","Your username and password is correct")
    else:
        messagebox.showwarning("Input passed","You have enter"+user.get()+"  "+password.get())


windows=Tk()
windows.title("LOGIN FORM")
#windows.geometry("600x400")
windows.resizable(False,False)

user=StringVar()
password=StringVar()

L1=Label(windows,text="LOGIN",font=("Arial",18,"bold"))
L1.pack(pady=20)

L2=Label(windows,text="Username",font=("Arial",14,"bold"))
L2.pack(padx=20,pady=10)

E1=Entry(windows,font=("Arial",14,"normal"),textvariable=user)
E1.pack(padx=10)

L3=Label(windows,text="Password",font=("Arial",14,"bold"))
L3.pack()

E2=Entry(windows,font=("Arial",14,"normal"),show="*",textvariable=password)
E2.pack(padx=10)

Button=Button(windows,text="Log-in",font=("Arial",16,"bold"),padx=10,pady=5,command=login_Function)
Button.pack(pady=10)

window=mainloop()