from tkinter import *

root = Tk()
root.title('Grid')

myLabel = Label(root, text='Hello World')
myLabel2 = Label(root, text='My Name is DJanczak')
myLabel3 = Label(root, text='and I am a Danolog')

myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)
myLabel3.grid(row=2, column=2)

#Albo w jednym kroku (mniej czysty kod)
myLabel4 = Label(root, text='learning how to make an interface').grid(row=1, column=3)


root.mainloop()

