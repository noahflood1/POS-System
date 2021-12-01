'''
Commands for controlling the UI
'''

from tkinter import *
from tkinter.font import Font
from random import *
import csv
from code import Bank_Account

#----------------------------------------------------
#Inventory List Methods

#List of all inventory items - all objects are of the item class
inventoryList = []

#temportary function for printing the inventory list
def printInventoryList():
    print("Inventory:")
    count = 1
    for item in inventoryList:
        print(count)
        print("{}\n".format(item.toString()))
        count+=1

#function that instantiates and adds a new Item object to the inventoryList based on the three necessary parameters which are stored in a list
def addToInventoryList(new_Item_paramaters):
    new_item = Item(new_Item_paramaters[0], new_Item_paramaters[1], new_Item_paramaters[2])
    inventoryList.append(new_item)
    #print(new_item.toString())    for testing

#Function taking in the name of an Item and deleting it from the list of inventory item
#The Function creates a temporary dictionary to determine the index of the item to be deleted
def deleteFromInventoryList(itemIndex):
  tempDict={}
  count=0
  for item in inventoryList:
    tempDict.update({item.name:count})
    count+=1
  inventoryList.pop(tempDict.get(itemIndex))

#function for getting a new listbox object with all of the items in inventory list
def getFramedInventoryList(master_frame):

    inventory_listbox = Listbox(master_frame)

    for item in inventoryList:
        item_text = "{name:<15}{stock:<5}{price:>6}".format(name=item.name, stock=item.stock, price=item.price)
        print(item_text)
        inventory_listbox.insert("end", item_text)
    print('Why is this not formatted correctly on screen????')

    return inventory_listbox

#updates changes to the inventory listbox object on screen
def updateFramedInventoryList(Listbox):
    Listbox.delete(0, 'end')

    for item in inventoryList:
        item_text = "{name:<15}{stock:<5}{price:>6}".format(name=item.name, stock=item.stock, price=item.price)
        print(item_text)
        Listbox.insert("end", item_text)
    print('Why is this not formatted correctly on screen????')

#----------------------------------------------------
#Item class - Container for name, stock, and price of items
class Item:

  #constructor method
  def __init__(self, name, stock, price, cart=0):
    self.name = name
    self.stock = stock
    self.price = price
    self.cart = cart
    
  #change price of an item
  def changePrice(self, price):
    self.price = price

  #change the amount of an item
  def changeAmount(self, newAmount):
    self.stock = newAmount

  #using an item object and an amount returns the price of amount of item
  def buyItem(self, amount):
    return(self.price * amount)
  
  def setCart(self, cart):
    self.cart = cart

  #toString method for Item objects
  def toString(self):
    result = 'Item: ' + self.name + '\nStock: ' + str(self.stock) + '\nPrice: $' + str(self.price)
    return result


#----------------------------------------------------
#file commands allowing for saved data

file_path = 'files/products.csv'

#function that updates the csv file based on the inventoryList object (re-writes it entirely)
def update_file():
    with open(file_path, 'w', newline='') as f: #opens a file based on a path, with intent to "write" with the 'w' parameter. 'f' is the file
        thewriter = csv.writer(f)

        #now, we can actually write rows of the csv file with a list, where every item in the list is a column item in the file
        for item in inventoryList:
            #for every Item in the inventoryList, create a little list called "item_list" that contains the item's name, stock, and price
            item_list = []          
            item_list.append(item.name)
            item_list.append(item.stock)
            item_list.append(item.price)

            thewriter.writerow(item_list)

#function that initializes the inventoryList from the csv file
def load_list():
    with open(file_path, 'r') as f: #opens a file based on a path, with intent to "read" with the 'r' parameter. 'f' is the file
        thereader = csv.reader(f)

        #for every line in the file, parse each item from the line to instantiate a new Item object, and add that object to the inventoryList
        for line in thereader:
            new_item = Item(line[0], line[1], line[2])
            inventoryList.append(new_item)


#----------------------------------------------------
#new functions for having different frames/windows

def show_frame(frame):
#this brings the parameter frame to the 'front' so that we can see it and click its contents
  frame.tkraise()

def quit(win):
  win.destroy()

#----------------------------------------------------
#Restock methods
def restock(a,b,c,d,e):
  Bank_Account.restockDate(b,c,d,e)
  tempDict={}
  count=0
  for item in inventoryList:
    tempDict.update({item.name:count})
    count+=1
  inventoryList[tempDict.get(a)].stock =int(b) + int(inventoryList[tempDict.get(a)].stock)
  update_file()
  
  
#----------------------------------------------------
#main code for testing

def getItemFromList(itemName):
  tempDict={}
  count=0
  for item in inventoryList:
    tempDict.update({item.name:count})
    count+=1
  return(inventoryList[tempDict.get(itemName)])


'''
a = 'beans'
b = 20
c = 3.25

super_new_item = Item(a, b ,c)

inventoryList.append(super_new_item)
inventoryList.append(Item("jones", 3, 6))
inventoryList.append(Item("apples", 10, 2.5))

update_file()
'''