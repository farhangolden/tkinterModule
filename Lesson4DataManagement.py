from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
'''
with open("emp.csv","w",newline="") as f1:
    csvWriter=csv.writer(f1)
    csvWriter.writerow(["First Name","Last Name","Address","City","Gender","Education","Experience","Job Profile","Department","Skills","Basic","Allownces","Gross_Salary","Tax","Net Salary"])
    f1.close()
    print("File Created!")
'''
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

    basic_salary=int(salary.get())
    allownces=basic_salary*0.2
    gross_salary=(allownces+basic_salary)*12
    if gross_salary>=1200000:
        tax=gross_salary*0.1
    elif gross_salary>=800000:
        tax=gross_salary*0.08
    elif gross_salary>=600000:
        tax=gross_salary*0.06
    elif gross_salary>=400000:
        tax=gross_salary*0.04
    else:
        tax=0

    net_salary=gross_salary-tax

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
    
    basic=salary.get()

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
    print(f"Basic: {basic_salary} \n Allownces: {allownces} \n Gross: {gross_salary} \n Tax: {tax} \n Net: {net_salary} \n")
    with open("emp.csv","a",newline="") as f2:
        csvWriter=csv.writer(f2)
        csvWriter.writerow([firstname,lastname,add,g,cty,educate,exp,jobp,depart,my_skills,basic_salary,allownces,gross_salary,tax,net_salary])
        messagebox.showinfo("Data Stored","One Recort Added To The File")
        f2.close()

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
salary=StringVar()

edu_selected=StringVar()
education_list=["HSC","B.Com","B.Tech","BCA","B.Sc","B.E","M.Sc","MCA"]
edu_selected.set(education_list[0])

exp_selected=StringVar()
exp_list=list(range(1,16))
exp_selected.set(exp_list[0])


L1=Label(root,text="Employees Detail",font=("Calibri",20,"bold"))
L1.grid(row=0,column=0,columnspan=2,padx=10,pady=10)

L2=Label(root,text="Enter First Name: ",font=("Calibri",14,"bold"))
L2.grid(row=1,column=0)

L3=Label(root,text="Enter Last Name: ",font=("Calibri",14,"bold"))
L3.grid(row=1,column=1)

L3=Label(root,text="Enter Address: ",font=("Calibri",14,"bold"))
L3.grid(row=6,column=2)

E1=Entry(root,font=("Calibri",14,"normal"),textvariable=address)
E1.grid(row=7,column=2,padx=10,pady=10)

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

E9=Entry(root,font=("Calibri",14,"normal"),textvariable=salary)
E9.grid(row=14,columnspan=2,padx=10,pady=10)

B1=Button(root,text="Submit",command=submit_data,font=("Calibri",14,"bold"),padx=15,pady=5)
B1.grid(row=15,columnspan=2,padx=15,pady=5)

root.mainloop()
