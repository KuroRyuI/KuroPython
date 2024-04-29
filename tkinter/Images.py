from tkinter import *

#package for images - "Pillow"
from PIL import ImageTk, Image

root = Tk()
root.title('Images')

#
#root.geometry("800x700")
#

#FAVICON !!!!!! :D
root.iconbitmap('C:/Users/danie/Desktop/New folder/favicon.ico')

#trzeba obejsc pythona w taki sposob zeby wyswietlac obrazy
my_img1 = ImageTk.PhotoImage(Image.open("C:/Users/danie/Desktop/New folder/123.jpg").resize((300, 450)))
#resizing wymusza na obrazie dostosowanie sie do wymiarow, nie zoomuje
my_img2 = ImageTk.PhotoImage(Image.open("C:/Users/danie/Desktop/New folder/1234.jpg").resize((400, 450)))
my_img3 = ImageTk.PhotoImage(Image.open("C:/Users/danie/Desktop/New folder/12345.PNG"))
my_img4 = ImageTk.PhotoImage(Image.open("C:/Users/danie/Desktop/New folder/123456.PNG"))
my_img5 = ImageTk.PhotoImage(Image.open("C:/Users/danie/Desktop/New folder/1234567.PNG"))
image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = Label(image=image_list[0])
my_label.grid(row=0, column=0, columnspan=12)
number = 1

def back(image_number):
    global my_label, button_forward, button_back, number, status
    number -= 1
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    my_label.grid(row=0, column=0, columnspan=12)
    button_forward.grid_forget()
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back.grid_forget()
    button_back = Button(root, text='<<', command=lambda: back(image_number - 1))
    if image_number == 1:
        button_back = Button(root, text='<<', state=DISABLED)

    button_back.grid(row=2, column=0)
    button_forward.grid(row=2, column=2)
    status.grid_forget()
    status = Label(root, text=f"Image: {number}/{len(image_list)}", relief=SUNKEN, anchor=W)
    status.grid(row=1, column=0, columnspan=12, sticky=W)


def forward(image_number):
    global my_label, button_forward, button_back, number, status
    number += 1
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    my_label.grid(row=0, column=0, columnspan=12)
    button_forward.grid_forget()
    button_forward = Button(root, text=">>", command=lambda: forward(image_number+1))
    button_back.grid_forget()
    button_back = Button(root, text='<<', command=lambda: back(image_number-1))
    if image_number == len(image_list):
        button_forward = Button(root, text='>>', state=DISABLED)

    button_back.grid(row=2, column=0)
    button_forward.grid(row=2, column=2)
    status.grid_forget()
    status = Label(root, text=f"Image: {number}/{len(image_list)}", relief=SUNKEN, anchor=W)
    status.grid(row=1, column=0, columnspan=12, sticky=E)


button_back = Button(root, text='<<', command=lambda: back(1), state=DISABLED)
button_back.grid(row=2, column=0)

button_quit = Button(root, text='exit program', command=root.quit)
button_quit.grid(row=2, column=1)

button_forward = Button(root, text='>>', command=lambda: forward(2))
button_forward.grid(row=2, column=2)

status = Label(root, text=f"Image: {number}/{len(image_list)}", relief=SUNKEN, anchor=W)
status.grid(row=1, column=0, columnspan=12, sticky=E)
root.mainloop()
