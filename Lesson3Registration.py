from tkinter import *
from tkinter import messagebox
import csv
'''
with open("register.csv","w",newline="") as f1:
    csvWriter=csv.writer(f1)
    csvWriter.writerow(["First Name","Last Name","Address","City","Gender","Hobbies","Password"])
'''
def submit_data():
    if fname.get()=="" or lname.get()=="" or address.get()=="" or city.get()=="" or pass1value.get()=="" or pass2value.get()=="":
        messagebox.showerror("Invalid or missing input","Please Enter All Values!")
    elif pass1value.get()!=pass2value.get():
        messagebox.showerror("Password Error!","Password Does Not Match")
    else:

        firstname=fname.get()
        lastname=lname.get()
        add=address.get()
        cty=city.get()
        g=gender.get()
        hobbies=""
        if cricket.get():
            hobbies+="Cricket"
        else:
            pass
        if football.get():
            hobbies+="FootBall"
        else:
            pass
        if chess.get():
            hobbies+="Chess"
        else:
            pass

        passwd=pass1value.get()

        RegData=[firstname,lastname,add,g,cty,hobbies,passwd]
        with open("register.csv","a",newline="") as f1:
            csvWriter=csv.writer(f1)
            csvWriter.writerow(RegData)
            messagebox.showinfo("New Record","One Record Added To File!")
            E1.delete(0,END)
            E2.delete(0,END)
            E3.delete(0,END)
            E4.delete(0,END)
            E5.delete(0,END)
            E6.delete(0,END)



def ShowHidePass1():
    if mypass1.get():
        E5.config(show="")
    else:
        E5.config(show="*")

def ShowHidePass2():
    if mypass2.get():
        E6.config(show="")
    else:
        E6.config(show="*")


root=Tk()
root.title("Students Registration")
root.resizable(False,False)

gender=StringVar()
mypass1=BooleanVar()
mypass2=BooleanVar()
fname=StringVar()
lname=StringVar()
address=StringVar()
city=StringVar()
cricket=BooleanVar()
football=BooleanVar()
chess=BooleanVar()
pass1value=StringVar()
pass2value=StringVar()


L1=Label(root,text="Student Registartion",font=("Calibri",18,"bold"))
L1.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

L2=Label(root,text="Enter First Name: ",font=("Calibri",14,"bold"))
L2.grid(row=1,column=0)

L3=Label(root,text="Enter Last Name: ",font=("Calibri",14,"bold"))
L3.grid(row=1,column=1)

E1=Entry(root,font=("Calibri",14,"normal"),textvariable=fname)
E1.grid(row=2,column=0,padx=10,pady=10)

E2=Entry(root,font=("Calibri",14,"normal"),textvariable=lname)
E2.grid(row=2,column=1,padx=10,pady=10)

L4=Label(root,text="Enter Address: ",font=("Calibri",14,"bold"))
L4.grid(row=3,column=0)

L5=Label(root,text="Enter City: ",font=("Calibri",14,"bold"))
L5.grid(row=3,column=1)

E3=Entry(root,font=("Calibri",14,"normal"),textvariable=address)
E3.grid(row=4,column=0,padx=10,pady=10)

E4=Entry(root,font=("Calibri",14,"normal"),textvariable=city)
E4.grid(row=4,column=1,padx=10,pady=10)

L6=Label(root,text="Select Gender",font=("Calibri",18,"bold"))
L6.grid(row=5,columnspan=2,padx=10,pady=10)

L7=Label(root,text="Male",font=("Calibri",14,"normal"))
L7.grid(row=6,column=0)

L8=Label(root,text="Female",font=("Calibri",14,"normal"))
L8.grid(row=6,column=1)

R1=Radiobutton(root,value="Male",variable=gender)
R1.grid(row=7,column=0)

R2=Radiobutton(root,value="Female",variable=gender)
R2.grid(row=7,column=1)

L9=Label(root,text="Select Hobbies",font=("Calibri",18,"bold"))
L9.grid(row=8,columnspan=2,padx=10,pady=10)

Cb1=Checkbutton(root,text="Cricket",font=("Calibry",14,"bold"),variable=cricket)
Cb1.grid(row=9,column=0)

Cb2=Checkbutton(root,text="FootBall",font=("Calibry",14,"bold"),variable=football)
Cb2.grid(row=10,column=0)

Cb3=Checkbutton(root,text="Chess",font=("Calibry",14,"bold"),variable=chess)
Cb3.grid(row=11,column=0)

L10=Label(root,text="Type Password",font=("Calibri",18,"bold"))
L10.grid(row=12,columnspan=2)

E5=Entry(root,font=("Calibri",14,"normal"),show="*",textvariable=pass1value)
E5.grid(row=13,column=0,padx=10,pady=10)

cb4=Checkbutton(root,text="Show/Hide Password",variable=mypass1,font=("Calibri",14,"bold"),command=ShowHidePass1)
cb4.grid(row=13,column=1)

L11=Label(root,text="Verify Password",font=("Calibri",18,"bold"))
L11.grid(row=14,columnspan=2)

E6=Entry(root,font=("Calibri",14,"normal"),show="*",textvariable=pass2value)
E6.grid(row=15,column=0,padx=10,pady=10)

cb5=Checkbutton(root,text="Show/Hide Password",variable=mypass2,font=("Calibri",14,"bold"),command=ShowHidePass2)
cb5.grid(row=15,column=1)

B1=Button(root,text="Submit",command=submit_data,font=("Calibri",14,"bold"),padx=15,pady=5)
B1.grid(row=16,columnspan=2,padx=15,pady=5)

root=mainloop()
