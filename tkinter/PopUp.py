from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


root = Tk()
root.title('Frames')

root.iconbitmap('C:/Users/danie/Desktop/New folder/favicon.ico')

#inside padding
frame = LabelFrame(root, text='', padx=10,pady=10)
#outside padding
frame.grid(row=0, column=0)

def popup():
# showinfo, showwarning, showerror, askquestion, askokcancel,askyesno
    messagebox.showerror("jumpSCARE!", "BUGA BUGA!")
    response = messagebox.askyesno("jumpSCARE!", "Are you scared :3?")
    if response == 1:
        Label(frame, text="hahaha!").pack()
    else:
        Label(frame, text=':o').pack()

Button(frame, text='Jestem jump scarem!', command=popup).pack()


my_img1 = ImageTk.PhotoImage(Image.open("C:/Users/danie/Desktop/New folder/123.jpg").resize((300, 450)))
my_label = Label(frame, image=my_img1)
my_label.pack()

root.mainloop()
