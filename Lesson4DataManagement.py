from tkinter import *
from tkinter import ttk

def submit_data():
    firstname=fname.get()
    lastname=lname.get()
    add=address.get()
    cty=city.get()
    g=gender.get()
    educate=edu_selected.get()
    exp=exp_selected.get()
    jobp=job_profile.get()
    depart=department.get()
    my_skills=[]

    if skill1.get():
        my_skills.append("Python")
    else:
        pass
    if skill2.get():
        my_skills.append("Excel")
    else:
        pass
    if skill3.get():
        my_skills.append("JavaScript")
    else:
        pass
    
    basic=basic_salary.get()

    EmpData=[firstname,lastname,add,g,cty,educate,exp,jobp,depart,skill1,skill2,skill3,basic]

    print("First Name: ",firstname)
    print("Last Name: ",lastname)
    print("Address: ",add)
    print("Gender: ",g)
    print("City: ",cty)
    print("Education: ",educate)
    print("Experience: ",exp)
    print("Job Profile: ",jobp)
    print("Department: ",depart)
    print("Skills: ",my_skills)
    print("Basic Salary: ",basic)

root=Tk()
root.title("Employees Job")
#windows.geometry("600x400")
root.resizable(False,False)

gender=StringVar()
fname=StringVar()
lname=StringVar()
address=StringVar()
city=StringVar()
job_profile=StringVar()
department=StringVar()
skill1=BooleanVar()
skill2=BooleanVar()
skill3=BooleanVar()

edu_selected=StringVar()
education_list=["HSC","B.Com","B.Tech","BCA","B.Sc","B.E","M.Sc","MCA"]
edu_selected.set(education_list[0])

exp_selected=StringVar()
exp_list=list(range(1,16))
exp_selected.set(exp_list[0])




basic_salary=StringVar()

L1=Label(root,text="Employees Detail",font=("Calibri",20,"bold"))
L1.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

L2=Label(root,text="Enter First Name: ",font=("Calibri",14,"bold"))
L2.grid(row=1,column=0)

L3=Label(root,text="Enter Last Name: ",font=("Calibri",14,"bold"))
L3.grid(row=1,column=1)

E1=Entry(root,font=("Calibri",14,"normal"),textvariable=fname)
E1.grid(row=2,column=0,padx=10,pady=10)

E2=Entry(root,font=("Calibri",14,"normal"),textvariable=lname)
E2.grid(row=2,column=1,padx=10,pady=10)

L4=Label(root,text="Gender",font=("Calibri",18,"bold"))
L4.grid(row=3,column=0,columnspan=2,padx=10,pady=10)

L5=Label(root,text="Male",font=("Calibri",14,"normal"))
L5.grid(row=4,column=0)

L6=Label(root,text="Female",font=("Calibri",14,"normal"))
L6.grid(row=4,column=1)

R1=Radiobutton(root,value="Male",variable=gender)
R1.grid(row=5,column=0)

R2=Radiobutton(root,value="Female",variable=gender)
R2.grid(row=5,column=1)

L7=Label(root,text="Enter City: ",font=("Calibri",14,"bold"))
L7.grid(row=6,column=0)

L8=Label(root,text="Select Education: ",font=("Calibri",14,"bold"))
L8.grid(row=6,column=1)

E4=Entry(root,font=("Calibri",14,"normal"),textvariable=city)
E4.grid(row=7,column=0,padx=10,pady=10)

op1=ttk.Combobox(root,font=("Calibri",14,"normal"),textvariable=edu_selected,values=education_list)
op1.grid(row=7,column=1,padx=10,pady=10)


L9=Label(root,text="Select Experience: ",font=("Calibri",14,"bold"))
L9.grid(row=8,column=0)

L10=Label(root,text="Enter Job Profile: ",font=("Calibri",14,"bold"))
L10.grid(row=8,column=1)

op2=ttk.Combobox(root,font=("Calibri",14,"normal"),textvariable=exp_selected,value=exp_list)
op2.grid(row=9,column=0,padx=10,pady=10)

E6=Entry(root,font=("Calibri",14,"normal"),textvariable=job_profile)
E6.grid(row=9,column=1,padx=10,pady=10)

L11=Label(root,text="Enter Department: ",font=("Calibri",14,"bold"))
L11.grid(row=10,column=0)

L12=Label(root,text="Select Skill: ",font=("Calibri",14,"bold"))
L12.grid(row=10,column=1)

E7=Entry(root,font=("Calibri",14,"normal"),textvariable=department)
E7.grid(row=11,column=0,padx=10,pady=10)

cb1=Checkbutton(root,text="Python",variable=skill1)
cb1.grid(row=12,column=0,padx=10,pady=10)

cb2=Checkbutton(root,text="Excel",variable=skill2)
cb2.grid(row=12,column=1,padx=10,pady=10)

cb3=Checkbutton(root,text="JavaScript",variable=skill3)
cb3.grid(row=12,column=2,padx=10,pady=10)

L13=Label(root,text="Basic Salary: ",font=("Calibri",14,"bold"))
L13.grid(row=13,columnspan=2)

E9=Entry(root,font=("Calibri",14,"normal"),textvariable=basic_salary)
E9.grid(row=14,columnspan=2,padx=10,pady=10)

B1=Button(root,text="Submit",command=submit_data,font=("Calibri",14,"bold"),padx=15,pady=5)
B1.grid(row=15,columnspan=2,padx=15,pady=5)

root.mainloop()