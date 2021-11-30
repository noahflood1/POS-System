

from tkinter import *
from tkinter.font import Font
from random import *

#Item class - Container for name, stock, and price of items
class Item:
  #constructor method
  def __init__(self, name, stock, price):
    self.name = name
    self.stock = stock
    self.price = price

  #change price of an item
  def changePrice(self, price):
    self.price = price

  #using an object and an amount returns the price of amount of item
  def buyItem(self, amount):
    return(self.price * amount)

  def toString(self):
    result = 'Item: ' + self.name + '\nStock: ' + str(self.stock) + '\nPrice: $' + str(self.price)
    return result


#----------------------------------------------------
#Button Commands

#adds an item to the item list
def addItem(name, stock, price):
  itemList.append(Item(name,stock,price))

#deletes the item with the entered value
def delItem(itemIndex):
  tempDict={}
  count=0
  for item in itemList:
    tempDict.update({item.name:count})
    count+=1
  itemList.pop(tempDict.get(itemIndex))

'''
#NOT CALLED
'''
#lists each item, and its index in the list
def listItems():
  count = 0
  listtl=Toplevel()
  lb = Listbox(listtl)

  for item in itemList:
    lb.insert(count,item.name)
    count +=1
  lb.pack()

#List of all stock items - all objects of the item class
itemList = []


#----------------------------------------------------
#FILE COMMANDS ALLOWING FOR SAVED DATA
import csv
def rewriteFile():
    f = open('products.csv','w')
    f.write('')
    f.close()

def addToFile():
    with open('products.csv', 'w', newline='') as csvfile: 
      csvwriter = csv.writer(csvfile)
      for item in itemList:
        temp = [item.name, item.stock, item.price]
        csvwriter.writerow(temp)

def readFile():    
    with open('products.csv', newline='') as csvfile:
      reader = csv.reader(csvfile, delimiter=' ')
      count = 0
      for row in reader:
        temp = row[0].split(',')
        itemList.append(Item(temp[0],temp[1],temp[2]))
        count +=1 #count tracks row


#----------------------------------------------------
#Window Creation Methods (old methods)

#Creates a new window with 3 entry fields and adds an item to the item list.
def addWindow():
  def addItemEntry():
    a = str(ent1.get())
    b = int(ent2.get())
    c = float(ent3.get())
    addItem(a,b,c)
    tl.destroy()
  tl=Toplevel()
  text=Label(tl, text='Enter name, stock, and price of item\nThe Window will close if successfully added')
  ent1= Entry(tl)
  ent2= Entry(tl)
  ent3= Entry(tl)
  butto= Button(tl, text='add', command=addItemEntry, background="black", fg='white', height=2, width=10)
  
  text.pack()
  ent1.pack()
  ent2.pack()
  ent3.pack()
  butto.pack()

def delWindow():
  def delItemEntry():
    a = ent.get()
    delItem(a)
    deltl.destroy()
  deltl = Toplevel()
  text=Label(deltl, text='Enter name of item to delete\nWindow will close if successful')
  ent=Entry(deltl)
  button = Button(deltl, text='Delete',command=delItemEntry,background="black", fg = 'white',height=2,width=10)

  text.pack()
  ent.pack()
  button.pack()

#NEW FUNCTIONS FOR HAVING DIFFERENT WINDOWS/FRAMES------------------------------------

def show_frame(frame):
  frame.tkraise() #this brings the parameter frame to the 'front' so that we can see it and click its contents

#----------------------------------------------------
#main window creation functions

def mainWin(): #Defines UI in terms of a window with widgets

  readFile()

  def quitProgram():
    #quits program and writes the itemList to a file
    win.destroy()
    addToFile()

  #STARTS LOOP: creating the main window and storing the window object in 'win'-------------------------------
  win=Tk() 
  win.title('POS system')
  win.geometry("800x600")
  win.config(bg='black')
  #GEOMETRY OF WINDOW
  window_height = 800
  window_width = 600
  #contrict size of window
  win.minsize(window_height, window_width)
  win.maxsize(window_height, window_width)

  #Allows for thins to be placed in window using grid, not sure why
  win.rowconfigure(0, weight=1)
  win.columnconfigure(0, weight=1)

  #define fonts to stylize text
  title_font = Font(
      family="Helvetica",
      size= 30,
      weight='bold'
      )
  
  big_font = Font(
    family="Helvetica",
    size=20,
    weight='bold'
  )

  text_font = Font(
    family="Helvetica",
    size=15,
  )

  #Code for all the windows--------------------------------------------------------------

  #Define frames that are the different "screens"
  main_frame = Frame(win)
  inventory_frame = Frame(win)
  add_delete_frame = Frame(win)
  stocks_frame = Frame(win)
  inevtory_frame = Frame(win)

  #FIXME: Add all the frames into this loop so that they exist in the window
  for frame in (main_frame, inventory_frame):
    frame.grid(row=0, column=0, stick='nsew') #does grid() to all these frames. only the last one grided shows; this is fixed with the function show_frame() above
  

  #main_frame code---------------------------------
  #title label
  titleLabel = Label(main_frame, text='POS System', bg='#4dd2ff', fg='black', font=title_font)
  titleLabel.pack(fill='x', ipady='10', pady='10')

  #menu label
  myLabel = Label(main_frame, text="Menu:", font=big_font)
  myLabel.pack(pady = 10)

  #inventory button
  btn1 = Button(main_frame, text='Inventory', command=listItems, background="black", fg='white', height=2, width=10, font=text_font)
  btn1.pack(pady=10)

  #Button to add a thing
  btn2 = Button(main_frame, text='Add Item', command=addWindow, background="black", fg='white', height=2, width=10, font=text_font)
  btn2.pack(pady=10)

  #Button to delete a thing
  btn3 = Button(main_frame, text='Delete Item', command=delWindow, background="black", fg='white', height=2, width=10, font=text_font)
  btn3.pack(pady=10)

  #Button to quit the program
  quitButton = Button(main_frame, text='Save & Quit', command=quitProgram, background="black", fg='white', height=2, width=10)
  quitButton.place(x=635, y=525)


  #invetory_frame code-----------------------------
  #header label
  inventory_header = Label(inventory_frame, text='Inventory', bg='#4dd2ff', fg='black', font=title_font)
  inventory_header.pack(fill='x', ipady='10', pady='10')

  #Button to go back
  back_button_inventory = Button(inventory_frame, text='Back', command=lambda:show_frame(main_frame), background="black", fg='white', height=2, width=10)
  back_button_inventory.place(x=635, y=525)







  show_frame(main_frame) #we want to start out seeing the title screen









#----------------------------------------------------
#All GUI functions occur between these two lines
mainWin()
mainloop()