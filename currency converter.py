from tkinter import *
from tkinter import ttk
from currency_converter import CurrencyConverter    

 
a=Tk()

a.title("Currency Converter")
font1 = ("Times", 30, "bold")
font2=("Times", 20)
font3=("Times", 15)
lable1=Label(a,font=font1,text="Currency Converter").grid(row=0, column=0, columnspan=2, pady=10)

label2=Label(a,font=font2,text="From").grid(row=1,column=0)

label3=Label(a,font=font2,text="To").grid(row=1,column=1)

currency=["INR","USD","CAD","CNY","DKK","EUR","GBP"]

def convert():
    from_currency=fmenu.get()
    to_currency=tmenu.get()
    amount = e.get()
    c=CurrencyConverter()
    converted_amount = c.convert(amount , from_currency , to_currency)
    converted_amount= round(converted_amount,2)
    txt.set(converted_amount)
    rl=Label(a,textvariable=txt,font=font2).grid(row=7,column=0, columnspan=2, pady=10)
    
def clear():
    e.delete(0,END)
txt=StringVar()


fmenu=ttk.Combobox(a,values=currency)
fmenu.grid(row=2,column=0)

tmenu=ttk.Combobox(a,values=currency)
tmenu.grid(row=2,column=1)

lable4=Label(a,font=font2,text="Enter Amount").grid(row=3,column=0, columnspan=2, pady=10)
e=Entry(a)
e.grid(row=4,column=0, columnspan=2, pady=10)

convertb=Button(a,text="Convert",command=convert, font=font3).grid(row=5,column=0, columnspan=2, pady=10)
clearb=Button(a,text="Clear",command=clear,font=font3).grid(row=6,column=0, columnspan=2, pady=10)

a.mainloop()
