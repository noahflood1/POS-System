from tkinter import *
from tkinter.font import Font
from random import *

root = Tk()
root.title("Test")
root.geometry("500x500")
root.config(bg='black')

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

main_frame = Frame(root, bg="red")
main_frame.grid(row=0, column=0, sticky='nsew')


root.mainloop()