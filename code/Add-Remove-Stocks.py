

#creates an inventory list to hold items
inventory = []

class Item:
  
  #constructor method
  def __init__(self, name, stock, price):
    self.name = name
    self.stock = stock
    self.price = price

  #gets the price of an item 
  def getPrice(self):
    return (self.price)

  #gets the name of an item
  def getName(self):
    return (self.name)

  #change price of an item
  def changePrice(self, price):
    if (price > 0):
      self.price = price
    else:
      print('Error: price cannot be less than zero.')
      return None

  #buys an item and reduces the inventory stock
  def buyItem(self, amount):
    if (amount > self.stock):
       print('Error: cannot buy more than current stock.')
       amount = 0
    else:
      self.stock -= amount
    return(self.price * amount)

  #adds an item to the inventory
  def addItem(self):
    inventory.append(self)

  #deletes an item from the inventory
  def delItem(self):
    inventory.pop(self)

  #changes the stock of an item
  def changeStock(self, stock):
    if (stock >=0):
      self.stock = stock
    else:
      print('Error: stock cannot be less than zero.')
      return None

  #gets the stock of an item
  def getItemStock(self):
     return(self.stock)

  #prints an item and its information
  def printItem(self):
    return('item:', self.name, 'stock:', self.stock, 'price:', self.price)

  #prints every item in the inventory
  def printInventory():
    output = ''
    for item in inventory:
      output += Item.printItem(item), '\n'
    return output

  #these threee functions might require a lamba function

  #sorts the inventory by item price
  #def sortInventoryByPrice():
    #return None
    #inventory.sort(key=lambda x: x.price)
                                  
  #sorts the inventory by item name
  #def sortInventoryByName():
    #return None
    #inventory.sort(key=lambda x: x.name)

  #sorts the inventory by an item's stock
  #def sortInventoryByStock():
    #return None
    #inventory.sort(key=lambda x: x:stock)

  #clears the inventory
  def clearInventory():
    inventory.clear()