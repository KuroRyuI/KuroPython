from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.title('Dialog')
root.iconbitmap('C:/Users/danie/Desktop/New folder/favicon.ico')

my_image = None  # Initialize my_image variable


def open():
    global my_image
    global my_image_label
    global my_label
    if my_image:
        my_image_label.pack_forget()  # Remove the previous image label if exists
        my_image = None  # Reset my_image variable
        my_label.pack_forget()

    root.filename = filedialog.askopenfilename(initialdir='', title='SELECT A FILE!',
                                               filetypes=(("png files", "*.png"), ("jpg files", "*.jpg")))
    if root.filename:  # Check if a file was selected
        my_label = Label(root, text=root.filename)
        my_label.pack()
        my_image = ImageTk.PhotoImage(Image.open(root.filename))
        my_image_label = Label(image=my_image)
        my_image_label.pack()


my_button = Button(root, text='open file', command=open)
my_button.pack()

root.mainloop()