from tkinter import *
from PIL import ImageTk, Image



root = Tk()
root.title('newWindow')
root.iconbitmap('C:/Users/danie/Desktop/New folder/favicon.ico')


def open():
    #jesli cos nie dziala dodaj jako globalna, moze akurat :3
    global my_img
    newWindow = Toplevel()
    newWindow.title('2nd Window')
    newWindow.iconbitmap('C:/Users/danie/Desktop/New folder/favicon.ico')
    my_img = ImageTk.PhotoImage(Image.open("C:/Users/danie/Desktop/New folder/1234.jpg").resize((400, 450)))
    my_label1 = Label(newWindow, image=my_img).pack()
    my_label = Label(newWindow, text='tada! I am in a new Window!', padx=10, pady=50).pack()
    button_quit = Button(newWindow, text='RUN!', padx=50, pady=50, command=newWindow.destroy).pack()

btn = Button(root, text='CLick to open a new Window', padx=50, pady=50, command=open, border = 20).pack()

root.mainloop()


