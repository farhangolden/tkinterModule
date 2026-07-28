from tkinter import *

def submit_data():
    pass

root=Tk()
root.title("Students Registration")
root.resizable(False,False)

gender=StringVar()

L1=Label(root,text="Student Registartion",font=("Calibri",18,"bold"))
L1.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

L2=Label(root,text="Enter First Name: ",font=("Calibri",14,"bold"))
L2.grid(row=1,column=0)

L3=Label(root,text="Enter Last Name: ",font=("Calibri",14,"bold"))
L3.grid(row=1,column=1)

E1=Entry(root,font=("Calibri",14,"normal"))
E1.grid(row=2,column=0,padx=10,pady=10)

E2=Entry(root,font=("Calibri",14,"normal"))
E2.grid(row=2,column=1,padx=10,pady=10)

L4=Label(root,text="Enter Address: ",font=("Calibri",14,"bold"))
L4.grid(row=3,column=0)

L5=Label(root,text="Enter City: ",font=("Calibri",14,"bold"))
L5.grid(row=3,column=1)

E3=Entry(root,font=("Calibri",14,"normal"))
E3.grid(row=4,column=0,padx=10,pady=10)

E4=Entry(root,font=("Calibri",14,"normal"))
E4.grid(row=4,column=1,padx=10,pady=10)

L6=Label(root,text="Select Gender",font=("Calibri",18,"bold"))
L6.grid(row=5,columnspan=2,padx=10,pady=10)

L7=Label(root,text="Male",font=("Calibri",14,"normal"))
L7.grid(row=6,column=0)

L8=Label(root,text="Female",font=("Calibri",14,"normal"))
L8.grid(row=6,column=1)

R1=Radiobutton(root,value="Male",textvariable=gender)
R1.grid(row=7,column=0)

R2=Radiobutton(root,value="Female",textvariable=gender)
R2.grid(row=7,column=1)

L9=Label(root,text="Select Hobbies",font=("Calibri",18,"bold"))
L9.grid(row=8,columnspan=2,padx=10,pady=10)

Cb1=Checkbutton(root,text="Cricket",font=("Calibry",14,"bold"))
Cb1.grid(row=9,column=0)

Cb2=Checkbutton(root,text="FootBall",font=("Calibry",14,"bold"))
Cb2.grid(row=10,column=0)

Cb3=Checkbutton(root,text="Chess",font=("Calibry",14,"bold"))
Cb3.grid(row=11,column=0)

L10=Label(root,text="Type Password",font=("Calibri",18,"bold"))
L10.grid(row=12,columnspan=2)

E5=Entry(root,font=("Calibri",14,"normal"),show="*")
E5.grid(row=13,columnspan=2,padx=10,pady=10)

L11=Label(root,text="Verify Password",font=("Calibri",18,"bold"))
L11.grid(row=14,columnspan=2)

E5=Entry(root,font=("Calibri",14,"normal"),show="*")
E5.grid(row=15,columnspan=2,padx=10,pady=10)

B1=Button(root,text="Submit",command=submit_data,font=("Calibri",14,"bold"),padx=15,pady=5)
B1.grid(row=16,columnspan=2,padx=15,pady=5)

root=mainloop()