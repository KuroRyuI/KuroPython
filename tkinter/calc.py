from tkinter import *

root = Tk()
root.title('Calc')

Uinput = Entry(root, width=50, borderwidth=20)
Uinput.grid(row=0, column=0, columnspan=3)


def button_click(number):
    current = Uinput.get()
    Uinput.delete(0, END)
    Uinput.insert(0, str(current) + str(number))


def clear():
    Uinput.delete(0, END)


def add():
    first_number= Uinput.get()
    global f_num, operation
    f_num = int(first_number)
    Uinput.delete(0, END)
    operation = 1


def sub():
    first_number = Uinput.get()
    global f_num, operation
    f_num = int(first_number)
    Uinput.delete(0, END)
    operation = 2

def equal():
    second_num = int(Uinput.get())
    Uinput.delete(0, END)
    if operation == 1:
        Uinput.insert(0, str(f_num+second_num))
    elif operation == 2:
        Uinput.insert(0, str(f_num-second_num))
    else:
        Uinput.insert(0, '0')




B_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
B_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
B_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
B_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
B_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
B_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
B_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
B_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
B_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
B_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

B_clear = Button(root, text="clear", padx=30, pady=20, command=clear)

B_add = Button(root, text="+", padx=40, pady=20, command=add)
B_subtract = Button(root, text="-", padx=40, pady=20, command=sub)
B_equal = Button(root, text="=", padx=40, pady=20, command=equal)

B_1.grid(row=3, column=0)
B_2.grid(row=3, column=1)
B_3.grid(row=3, column=2)
B_4.grid(row=2, column=0)
B_5.grid(row=2, column=1)
B_6.grid(row=2, column=2)
B_7.grid(row=1, column=0)
B_8.grid(row=1, column=1)
B_9.grid(row=1, column=2)
B_0.grid(row=4, column=1)
B_add.grid(row=5, column=0)
B_subtract.grid(row=5, column=1)
B_equal.grid(row=5, column=2)
B_clear.grid(row=4, column=2)



root.mainloop()
