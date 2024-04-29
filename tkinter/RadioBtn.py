from tkinter import *


root = Tk()
root.title('Frames')

root.iconbitmap('C:/Users/danie/Desktop/New folder/favicon.ico')

#inside padding
frame = LabelFrame(root, text='Wybierz pizze', padx=10, pady=10)
#outside padding
frame.grid(row=0, column=0)

r = IntVar()
r.set(1)

def clicked(value):
    myLabel = Label(frame, text=value)
    myLabel.pack()


Radiobutton(frame, text='Mala (30cm)', variable=r, value=1).pack()
Radiobutton(frame, text='Duża (40cm)', variable=r, value=2, command=lambda: clicked(r.get())).pack()

# wyświetl ustawioną wartość r
myLabel = Label(frame, text=r.get())
myLabel.pack()

My_Btn = Button(frame, text='Click me you hungry bastard!', command=lambda: clicked(r.get()))
My_Btn.pack()

#inside padding
frame2 = LabelFrame(root, text='Wybierz rodzaj', padx=10, pady=10)
#outside padding
frame2.grid(row=0, column=1, padx=100, pady=40)

my_list_of_toppings_on_pizza = [
    ("peperoni", "peperoni"),
    ("cheese", "cheese"),
    ("mushroom", "mushroom"),
    ("Onion", "mafiosa")
]

pizza = StringVar()
pizza.set('cheese')

for text, mode in my_list_of_toppings_on_pizza:
    Radiobutton(frame2, text=text, variable=pizza, value=mode).pack()

root.mainloop()
