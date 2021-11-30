'''
Program for outputting the actual User Interface with all of it's functions
@authors: 

Features Added:

Future Updates/ Fixes:
- screen change
- make text print to screen

Resources:
https://www.w3schools.com/colors/colors_picker.asp 

'''

from tkinter import *
import PyPDF2
from PIL import Image, ImageTk
import tkinter.messagebox

win = Tk()
win.title('POS System')
#win.configure(background='grey')
#win.geometry("582x600")

canvas = Canvas(win, width=600, height=300)
canvas.grid(columnspan=3, rowspan=6)


#dict for story inventory items (starts with some examples)
items = {
    'Bean Cans': 2452,
    'Coffee Cups': 1210,
    'Forks': 12312
}

#function for printing inventory ##Make this print to the actual UI and not terminal
def printInventory():
    print('-----Inventory-----')
    print(items)

#function for processing a transaction, might be an import statement in the future. placeholder for now
def Transaction():
    print('process transction function works')

""" #Logo (Can change to be whatever we want on home screen)
logo = Image.open('logo3.png')
logo = ImageTk.PhotoImage(logo)
logo_label = Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0) """

#Label
myLabel = Label(win, text="Menu:")
myLabel.grid(column=1, row=2)

#title label
titleLabel = Label(win, text='POS System', bg='#4dd2ff')
titleLabel.place(relx = 0.3, rely = 0, relheight=0.5, relheight=0.25)

#Buttons
btn1 = Button(win, text='Inventory', command=printInventory, background="black", fg='white', height=2, width=10)
btn1.grid(column=1,row=3)

btn2 = Button(win, text='Transaction', command=Transaction, background="black", fg='white', height=2, width=10)
btn2.grid(column=1,row=4)

btn3 = Button(win, text='test', font='Raleway', background='#20bebe', fg='white', height=2, width=15)
btn3.grid(column=1, row=5)

#End
win.mainloop()