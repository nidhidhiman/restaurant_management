import random
import time
from tkinter import *

root = Tk()
root.geometry("1600x800+0+0")
root.title("Resaurant System")

text_Input = StringVar()
operator = ""

first = Frame(root, width=1600, height=50, relief=SUNKEN)
first.pack(side=TOP)

f1 = Frame(root, width=800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width=300, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)

# name of the project on top
l1 = Label(first, font=('arial', 50, 'bold'), text="Resturent Management System", fg="steel Blue", bd=10, anchor='w')
l1.grid(row=0, column=0)

# time
local_time = time.asctime(time.localtime(time.time()))

# time show on the top
l1 = Label(first, font=('arial', 20, 'bold'), text=local_time, fg="steel Blue", bd=10, anchor='w')
l1.grid(row=1, column=0)

# calculator
t1 = Entry(f2, font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4, bg="powder blue",
           justify='right')
t1.grid(columnspan=4)


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)


def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")


def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""


def Exit():
    root.destroy()


def ref():
    a = random.randint(10908, 500876)
    randomRef = str(a)
    order.set(randomRef)
    # cof=Float(fries.get())


def Reset():
    order.set("")
    fries.set("")
    lunch.set("")
    burger.set("")
    pizza.set("")
    cheese.set("")
    drink.set("")
    cost.set("")
    service.set("")
    tax.set("")
    subt.set("")
    total.set("")


btn7 = Button(f2, padx=14, pady=14, fg="black", font=('arial', 20, 'bold'), text='7', bg="powder blue",
              command=lambda: btnClick(7), relief=SUNKEN).grid(row=2, column=0)
btn8 = Button(f2, padx=14, pady=14, fg="black", font=('arial', 20, 'bold'), text='8', bg="powder blue",
              command=lambda: btnClick(8), relief=SUNKEN).grid(row=2, column=1)
btn9 = Button(f2, padx=14, pady=14, fg="black", font=('arial', 20, 'bold'), text='9', bg="powder blue",
              command=lambda: btnClick(9), relief=SUNKEN).grid(row=2, column=2)
Addition = Button(f2, padx=13, pady=13, fg="black", font=('arial', 20, 'bold'), text='+', bg="powder blue",
                  command=lambda: btnClick('+'), relief=SUNKEN).grid(row=2, column=3)

btn4 = Button(f2, padx=14, pady=14, fg="black", font=('arial', 20, 'bold'), text='4', bg="powder blue",
              command=lambda: btnClick(4), relief=SUNKEN).grid(row=3, column=0)
btn5 = Button(f2, padx=14, pady=14, fg="black", font=('arial', 20, 'bold'), text='5', bg="powder blue",
              command=lambda: btnClick(5), relief=SUNKEN).grid(row=3, column=1)
btn6 = Button(f2, padx=14, pady=14, fg="black", font=('arial', 20, 'bold'), text='6', bg="powder blue",
              command=lambda: btnClick(6), relief=SUNKEN).grid(row=3, column=2)
subtraction = Button(f2, padx=13, pady=13, fg="black", font=('arial', 20, 'bold'), text='-', bg="powder blue",
                     command=lambda: btnClick('-'), relief=SUNKEN).grid(row=3, column=3)

btn1 = Button(f2, padx=14, pady=14, fg="black", font=('arial', 20, 'bold'), text='1', bg="powder blue",
              command=lambda: btnClick(1), relief=SUNKEN).grid(row=4, column=0)
btn2 = Button(f2, padx=14, pady=14, fg="black", font=('arial', 20, 'bold'), text='2', bg="powder blue",
              command=lambda: btnClick(2), relief=SUNKEN).grid(row=4, column=1)
btn3 = Button(f2, padx=14, pady=14, fg="black", font=('arial', 20, 'bold'), text='3', bg="powder blue",
              command=lambda: btnClick(3), relief=SUNKEN).grid(row=4, column=2)
multiplication = Button(f2, padx=13, pady=13, fg="black", font=('arial', 20, 'bold'), text='*', bg="powder blue",
                        command=lambda: btnClick('*'), relief=SUNKEN).grid(row=4, column=3)

btn0 = Button(f2, padx=14, pady=14, fg="black", font=('arial', 20, 'bold'), text='0', bg="powder blue",
              command=lambda: btnClick(0), relief=SUNKEN).grid(row=5, column=0)
clear = Button(f2, padx=14, pady=14, fg="black", font=('arial', 20, 'bold'), text='c', bg="powder blue",
               command=btnClearDisplay, relief=SUNKEN).grid(row=5, column=1)
equal = Button(f2, padx=14, pady=14, fg="black", font=('arial', 20, 'bold'), text='=', bg="powder blue",
               command=btnEquals, relief=SUNKEN).grid(row=5, column=2)
division = Button(f2, padx=14, pady=14, fg="black", font=('arial', 20, 'bold'), text='/', bg="powder blue",
                  command=lambda: btnClick('/'), relief=SUNKEN).grid(row=5, column=3)

# menuu
order = StringVar()
fries = StringVar()
lunch = StringVar()
burger = StringVar()
pizza = StringVar()
cheese = StringVar()
drink = StringVar()
cost = StringVar()
service = StringVar()
tax = StringVar()
subt = StringVar()
total = StringVar()

ml1 = Label(f1, font=('arial', 16, 'bold'), text="Order no.", bd=16, anchor='w')
ml1.grid(row=0, column=0)
tl1 = Entry(f1, font=('arial', 16, 'bold'), textvariable=order, bd=10, insertwidth=4, bg="powder blue", justify='right')
tl1.grid(row=0, column=1)

ml2 = Label(f1, font=('arial', 16, 'bold'), text="Fries meal", bd=16, anchor='w')
ml2.grid(row=1, column=0)
tl2 = Entry(f1, font=('arial', 16, 'bold'), textvariable=fries, bd=10, insertwidth=4, bg="powder blue", justify='right')
tl2.grid(row=1, column=1)

ml3 = Label(f1, font=('arial', 16, 'bold'), text="Lunch meal", bd=16, anchor='w')
ml3.grid(row=2, column=0)
tl3 = Entry(f1, font=('arial', 16, 'bold'), textvariable=lunch, bd=10, insertwidth=4, bg="powder blue", justify='right')
tl3.grid(row=2, column=1)

ml4 = Label(f1, font=('arial', 16, 'bold'), text="Burger meal", bd=16, anchor='w')
ml4.grid(row=3, column=0)
tl4 = Entry(f1, font=('arial', 16, 'bold'), textvariable=burger, bd=10, insertwidth=4, bg="powder blue",
            justify='right')
tl4.grid(row=3, column=1)

ml5 = Label(f1, font=('arial', 16, 'bold'), text="Pizza meal", bd=16, anchor='w')
ml5.grid(row=4, column=0)
tl5 = Entry(f1, font=('arial', 16, 'bold'), textvariable=pizza, bd=10, insertwidth=4, bg="powder blue", justify='right')
tl5.grid(row=4, column=1)

ml6 = Label(f1, font=('arial', 16, 'bold'), text="Cheese burger", bd=16, anchor='w')
ml6.grid(row=5, column=0)
tl6 = Entry(f1, font=('arial', 16, 'bold'), textvariable=cheese, bd=10, insertwidth=4, bg="powder blue",
            justify='right')
tl6.grid(row=5, column=1)

ml7 = Label(f1, font=('arial', 16, 'bold'), text="Drink", bd=16, anchor='w')
ml7.grid(row=0, column=2)
tl7 = Entry(f1, font=('arial', 16, 'bold'), textvariable=drink, bd=10, insertwidth=4, bg="powder blue", justify='right')
tl7.grid(row=0, column=3)

ml8 = Label(f1, font=('arial', 16, 'bold'), text="Cost", bd=16, anchor='w')
ml8.grid(row=1, column=2)
tl8 = Entry(f1, font=('arial', 16, 'bold'), textvariable=cost, bd=10, insertwidth=4, bg="powder blue", justify='right')
tl8.grid(row=1, column=3)

ml9 = Label(f1, font=('arial', 16, 'bold'), text="Service charge", bd=16, anchor='w')
ml9.grid(row=2, column=2)
tl9 = Entry(f1, font=('arial', 16, 'bold'), textvariable=service, bd=10, insertwidth=4, bg="powder blue",
            justify='right')
tl9.grid(row=2, column=3)

ml10 = Label(f1, font=('arial', 16, 'bold'), text="Tax", bd=16, anchor='w')
ml10.grid(row=3, column=2)
tl10 = Entry(f1, font=('arial', 16, 'bold'), textvariable=tax, bd=10, insertwidth=4, bg="powder blue", justify='right')
tl10.grid(row=3, column=3)

ml11 = Label(f1, font=('arial', 16, 'bold'), text="Subtotal", bd=16, anchor='w')
ml11.grid(row=4, column=2)
tl11 = Entry(f1, font=('arial', 16, 'bold'), textvariable=subt, bd=10, insertwidth=4, bg="powder blue", justify='right')
tl11.grid(row=4, column=3)

ml12 = Label(f1, font=('arial', 16, 'bold'), text="total", bd=16, anchor='w')
ml12.grid(row=5, column=2)
tl12 = Entry(f1, font=('arial', 16, 'bold'), textvariable=total, bd=10, insertwidth=4, bg="powder blue",
             justify='right')
tl12.grid(row=5, column=3)

# buttons: price, total, reset, exit

totalbtn = Label(f1, text="-----------", fg="white")
totalbtn.grid(row=7, columnspan=3)
totalbtn = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('arial', 16, 'bold'), width=10, text="TOTAL",
                  bg="powder blue", command=ref).grid(row=7, column=0)

resetbtn = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('arial', 16, 'bold'), width=10, text="RESET", bg="powder blue", command=Reset).grid(row=7, column=1)

exitbtn = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('arial', 16, 'bold'), width=10, text="EXIT", bg="powder blue", command=Exit)
exitbtn.grid(row=7, column=2)


def price():
    roo = Tk()
    roo.geometry("600x220+0+0")
    roo.title("Price List")
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
    lblinfo.grid(row=0, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="_____________", fg="white", anchor=W)
    lblinfo.grid(row=0, column=2)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
    lblinfo.grid(row=0, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Fries Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)
    lblinfo.grid(row=1, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Lunch Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="40", fg="steel blue", anchor=W)
    lblinfo.grid(row=2, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Burger Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=3, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Pizza Meal", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="50", fg="steel blue", anchor=W)
    lblinfo.grid(row=4, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cheese Burger", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="30", fg="steel blue", anchor=W)
    lblinfo.grid(row=5, column=3)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Drinks", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=0)
    lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="steel blue", anchor=W)
    lblinfo.grid(row=6, column=3)

    roo.mainloop()


pricebtn = Button(f1, padx=16, pady=8, bd=10, fg="black", font=('ariel', 16, 'bold'), width=10, text="PRICE",
                  bg="powder blue", command=price)
pricebtn.grid(row=7, column=3)

root.mainloop()
