'''
For processing transactions
'''
import tkinter as tk
from code import UI_commands2

#global variable about store
business_title = "Grandma's Bakery"
business_phone = "256-420-6969"

#variables for person using POS
customer_name = "Customer"
location = ''

#cart stuff
cartList = []

#variables for receipt
receipt_txt = "Test"
running_total = 0
subtotal = 0
total = 0

def updateCartList(item, amount): 
    #BIG FIX !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # INSTEAD OF APPENDING THE ITEM ONTO THE LIST OVER AND OVER, WE JUST RESET THE LIST COMPLETELY, THEN ADD EVERY ITEM 
    # FROM inventoryList TO THE cartList, AND WHEN WE UPDATE TOTAL, WE JUST LOOK AT THE amount_in_cart VALUE
    # FOR EVERY ITEM

    #print('Before:', UI_commands2.getItemFromList(item).cart)

    #First, update the cart value of the specified item by however much
    temp = UI_commands2.getItemFromList(item)
    temp.setCart(int(amount))

    #print('After:', UI_commands2.getItemFromList(item).cart)

    #Then, reset the cartList and add all the items back to the cart list 
    global cartList
    cartList = []

    for item in UI_commands2.inventoryList:
        #print(item.name)
        cartList.append(item)

    # Lastly, call the update_running_total function to change the running total based upon all the amount_in_cart values of the items
    update_running_total()


def update_running_total():
    global running_total
    #running_total = 0
    for item in cartList:
        #print(item.name, item.stock, item.price, item.cart, 'CARTLIST')

        item_X_amount_in_cart = (float(item.price) * float(item.cart))
        running_total += float(item_X_amount_in_cart)

def clearCart():
    #set every cart value in the cartlist to 0
    #set cartList to []
    global cartList
    for item in cartList:
        item.cart = 0
    cartList = []

#function that updates the running total on screen? do how you did it with update_inventroy list function in UI commansd
def update_running_total_label(string_var):
    print('running total before chaning sub_total',running_total)
    string_var.set('SUBTOTAL: ${}'.format(running_total))

#createing the receipt
def create_receipt():
    #write reciept_txt to file
    #print to console as well
    print(receipt_txt)
    return receipt_txt
    



