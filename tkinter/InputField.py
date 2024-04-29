from tkinter import *

root = Tk()
root.title('InputField')

myvar = StringVar()
myvar.set("Enter Your Name:  ")

#kasuje cokolwiek jest w oknie dialogowym po kliknięciu
def on_click(event):
    event.widget.delete(0, END)

def myClick():
    d = e.get()
    myLabel = Label(root, text=f'You clicked me {d}! :o')
    myLabel.pack()


e = Entry(root, textvariable=myvar, width=50, bg='green', fg='black', borderwidth=20)
e.bind("<Button-1>", on_click)
e.pack()

myButton = Button(root, text="dont click me :'( ", command=myClick)

myButton.pack()

root.mainloop()


