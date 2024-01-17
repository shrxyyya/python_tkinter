from tkinter import *
root=Tk()
root.title("Simple Calculator")

e=Entry(root, width=65, borderwidth=5)
e.grid(row=0, column=0, columnspan=3)

def button_click(number):
    e.delete(0, END)
    current=e.get()
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number=e.get()
    global f_num
    global math      #since we are required to do addition, subtraction, multiplication and division with only one button,i.e., '=' button, we need to declare a global variable for it.
    math="addition"
    f_num=int(first_number)     #we cannot use f_num=int(e.get()) and then use this f_num everywhere else bcoz then it'll store the first_number value as the first value we entered bcoz e.get() got the first enterd value, and this value didn't change in the memory.
    #we can't use f_num=int(e.get()) in other functions as 'f_num' only... bcoz:
    #eg: if i first entered 74 (i.e., first_number=74), and then clicked '+', so the f_num variable takes 74 as its value and keeps it like that for all the other functions as well even if we want to enter some other value for the first_number in that function
    e.delete(0, END)

def button_subtract():
    first_number=e.get()
    global f_num
    global math
    math="subtraction"
    f_num=int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number=e.get()
    global f_num
    global math
    math="multiplication"
    f_num=int(first_number)
    e.delete(0, END)

def button_divide():
    first_number=e.get()
    global f_num
    global math
    math="division"
    f_num=int(first_number)
    e.delete(0, END)

def button_equal():
    second_number=e.get()
    e.delete(0, END)
    if math=="addition":
        num_add=f_num + int(second_number)
        e.insert(0, num_add)
    elif math=="subtraction":
        num_subtract=f_num - int(second_number)
        e.insert(0, num_subtract)
    elif math=="multiplication":
        num_multiply=f_num * int(second_number)
        e.insert(0, num_multiply)
    elif math=="division":
        num_divide=f_num / int(second_number)
        e.insert(0, num_divide)


b1=Button(root, text="1", padx=60, pady=20, borderwidth=3, command=lambda: button_click(1))
b2=Button(root, text="2", padx=60, pady=20, borderwidth=3, command=lambda: button_click(2))
b3=Button(root, text="3", padx=60, pady=20, borderwidth=3, command=lambda: button_click(3))
b4=Button(root, text="4", padx=60, pady=20, borderwidth=3, command=lambda: button_click(4))
b5=Button(root, text="5", padx=60, pady=20, borderwidth=3, command=lambda: button_click(5))
b6=Button(root, text="6", padx=60, pady=20, borderwidth=3, command=lambda: button_click(6))
b7=Button(root, text="7", padx=60, pady=20, borderwidth=3, command=lambda: button_click(7))
b8=Button(root, text="8", padx=60, pady=20, borderwidth=3, command=lambda: button_click(8))
b9=Button(root, text="9", padx=60, pady=20, borderwidth=3, command=lambda: button_click(9))
b0=Button(root, text="0", padx=60, pady=20, borderwidth=3, command=lambda: button_click(0))
b_add=Button(root, text="+", padx=59, pady=20, borderwidth=3, command=button_add)
b_subtract=Button(root, text="-", padx=60, pady=20, borderwidth=3, command=button_subtract)
b_multiply=Button(root, text="*", padx=60, pady=20, borderwidth=3, command=button_multiply)
b_divide=Button(root, text="/", padx=60, pady=20, borderwidth=3, command=button_divide)
b_clear=Button(root, text="Clear", padx=117, pady=20, borderwidth=3, command=button_clear)
b_equals=Button(root, text="=", padx=59, pady=55, borderwidth=3, command=button_equal)


b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)
b0.grid(row=4, column=0)
b_add.grid(row=4, column=1)
b_subtract.grid(row=4, column=2)
b_multiply.grid(row=5, column=1)
b_divide.grid(row=5, column=2)
b_clear.grid(row=6, column=1, columnspan=2)
b_equals.grid(row=5, column=0, rowspan=2)


root.mainloop()