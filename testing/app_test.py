from tkinter import *
import PyPDF2
from PIL import Image, ImageTk

#Root Window
root = Tk()
root.title("Application")

#Canvas
canvas = Canvas(root, width=600,height=300, bg='blue')
canvas.grid(columns=3)

#Logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#Instructions
instructions = Label(root, text="Enter a PDF name to extract from", font='Raleway')
instructions.grid(columnspan=3, column=0, row=1)

#Browse button
browse_text = StringVar()
browse_btn = Button(root, textvariable=browse_text, font='Raleway')
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

#End
root.mainloop()