from tkinter import *


root = Tk()
root.title('Frames')

root.iconbitmap('C:/Users/danie/Desktop/New folder/favicon.ico')

#inside padding
frame = LabelFrame(root, text='My brand new frame...', padx=10,pady=10)
#outside padding
frame.pack(padx=40, pady=40)


#YOU CAN DO "GRID" IN FRAME !! WHILE HAVING "PACK"!! działają trochę jak "div" w html
btn = Button(frame, text="Don't you dare!")
btn.grid(row=1, column=1)
btn_2 = Button(frame, text="HA! I am here now!")
btn_2.grid(row=2, column=2)


root.mainloop()
