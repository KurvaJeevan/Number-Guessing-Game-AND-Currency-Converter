import random
from tkinter import *
from tkinter import ttk

a=Tk()
def Easy():

    k=random.randint(1,100)
    txt1.set("Find the number which is between 1-100")
    rl=Label(a,textvariable=txt1,font=font2).grid(row=6,column=0, columnspan=2, pady=10)
    enterb=Button(a,text="Enter",command=lambda:[Easyf(k),clear()],font=font3).grid(row=5,column=0, columnspan=2, pady=10)
    
def Easyf(k):    
    b=int(e.get())
    if b==k:
        txt2.set("     Congratulation! Your guess is right      ")
        r2=Label(a,textvariable=txt2,font=font2).grid(row=6,column=0, columnspan=2, pady=10)
        exit
    elif b<k:
        txt2.set("The number guessed is lower than the original number")
        r2=Label(a,textvariable=txt2,font=font2).grid(row=6,column=0, columnspan=2, pady=10)            
            
    else:
        txt2.set("The number guessed is higher than the original number")
        r2=Label(a,textvariable=txt2,font=font2).grid(row=6,column=0, columnspan=2, pady=10)
            
def Medium():

    k=random.randint(1,200)
    txt1.set("Find the number which is between 1-200")
    rl=Label(a,textvariable=txt1,font=font2).grid(row=6,column=0, columnspan=2, pady=10)
    enterb2=Button(a,text="Enter",command=lambda:[Easyf(k),clear()], font=font3).grid(row=5,column=0, columnspan=2, pady=10)
    
def Hard():

    k=random.randint(1,300)
    txt1.set("Find the number which is between 1-300")
    rl=Label(a,textvariable=txt1,font=font2).grid(row=6,column=0, columnspan=2, pady=10)
    enterb3=Button(a,text="Enter",command=lambda:[Easyf(k),clear()], font=font3).grid(row=5,column=0, columnspan=2, pady=10)
            
def start():
    c=compm.get()
    if c=="Easy":
        Easy()
    elif c=="Medium":
        Medium()
    elif c=="Hard":
        Hard()
    else:
        print("Select a complexity")

def clear():
    e.delete(0,END)

a.title("Number Guessing Game")
font1 = ("Times", 30, "bold")
font2=("Times", 20)
font3=("Times", 15)
lable1=Label(a,font=font1,text="Number Guessing Game").grid(row=0, column=0, columnspan=2, pady=10)

txt1=StringVar()
txt2=StringVar()
txt3=StringVar()


label2=Label(a,font=font2,text="Complexity").grid(row=1,column=0)

complexity=["Easy","Medium","Hard"]

compm=ttk.Combobox(a,values=complexity)
compm.grid(row=1,column=1)



startb=Button(a,text="Start",command=start, font=font3).grid(row=2,column=0, columnspan=2, pady=10)

lable4=Label(a,font=font2,text="Guess the Number").grid(row=3,column=0, columnspan=2, pady=10)

e=Entry(a)
e.grid(row=4,column=0, columnspan=2, pady=10)


a.mainloop()
