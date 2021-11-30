'''
Inventory.py creates a way to store and initialze amounts of stock items.
'''

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

itemList = []

#Methods below are for modifying the list of items

#adds an item to the item list
def addItem(name, stock, price):
  itemList.append(Item(name,stock,price))

#deletes the item in from the entered index
def delItem(itemIndex):
  itemList.pop(itemIndex)

#lists each item, and its index in the list
def listItems():
  count = 0
  for item in itemList:
    print(str(count) + ': ' + item.name)
    count +=1