from tkinter import *

root = Tk()
root.title('Buttons')

def myClick():
    myLabel = Label(root, text='You clicked me! :O')
    myLabel.grid(row=0, column=3)

myButton = Button(root, text="Don't click Me!", state=DISABLED)
myButton2 = Button(root, text='Click Me!', command=myClick)
mybutton3 = Button(root, text='I am bigger!', padx=50, pady=50)
myButton4 = Button(root, text='I am blue', bg='blue')
myButton5 = Button(root, text='My text is blue', fg='blue')


myButton.grid(row=0, column=0)
myButton2.grid(row=0, column=1)
mybutton3.grid(row=1, column=0, columnspan=2)
myButton4.grid(row=2, column=3)
myButton5.grid(row=3, column=3)




root.mainloop()





