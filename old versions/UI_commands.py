'''
Commands for controlling the UI
'''

from tkinter import *
from tkinter.font import Font
from random import *
import csv


#----------------------------------------------------

#List of all stock items - all objects of the item class
itemList = []

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

  #change the amount of an item
  def changeAmount(self, newAmount):
    self.stock = newAmount

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

''' Not called'''
#lists each item, and its index in the list
def listItems():
  count = 0
  listtl=Toplevel()
  lb = Listbox(listtl)

  for item in itemList:
    lb.insert(count,item.name)
    count +=1
  lb.pack()


#----------------------------------------------------
#Window Creation Methods (old methods)
#Creates a new window with 3 entry fields and adds an item to the item list.
def addWindow():

  def addItemEntry(): #redefined within frame code below
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


#----------------------------------------------------
#file commands allowing for saved data

file_path = 'files/products.csv'

def rewriteFile():
    f = open(file_path,'w')
    f.write('')
    f.close()

def addToFile():
    with open(file_path, 'w', newline='') as csvfile: 
      csvwriter = csv.writer(csvfile)
      for item in itemList:
        temp = [item.name, item.stock, item.price]
        csvwriter.writerow(temp)

def readFile():    
    with open(file_path, newline='') as csvfile:
      reader = csv.reader(csvfile, delimiter=' ')
      count = 0
      for row in reader:
        temp = row[0].split(',')
        itemList.append(Item(temp[0],temp[1],temp[2]))
        count +=1 #count tracks row

#---------------------------------------------
#new functions for having different frames/windows

def show_frame(frame):
  frame.tkraise() #this brings the parameter frame to the 'front' so that we can see it and click its contents

def list_items(frame): #new function for listing the items on the screen
  #show the list
  count = 0
  lb = Listbox(frame)
  lb.pack()
  #for every tiem in the list, insert it into the list box
  for item in itemList:
    lb.insert(count, item.name)
    count +=1
  lb.pack()

def load_inventory(): 
#conducted after something is added to the list, (when you press 'add')
#this writes all the items in itemList to the file, then reads the file back into the visual list in the inventory frame
  rewriteFile()
  addToFile()
  readFile()

def quit(win):
  win.destroy()


