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

def addToCartList(item, amount): #takes a string "item" that is the name of an existing item, takes a string "amount" that represents the amount of that item we want to add to cart.
    #change the item parameter's amount in cart value to "amount"
    #add that item to cartList
    yup = UI_commands2.getItemFromList(item)
    yup.setCart(int(amount))
    cartList.appent(yup)
    update_running_total()

def update_running_total():
    #for item in cartList
    #reset total
    #total += something
    #something item_total_cost
    global running_total
    for item in cartList:
        item_X_amount_in_cart = (item.price * item.cart)
        running_total += item_X_amount_in_cart

def clearCart():
    #set every cart value in the cartlist to 0
    #set cartList to []
    global cartList
    for item in cartList:
        item.cart = 0
    cartList = []

#function that updates the running total on screen? do how you did it with update_inventroy list function in UI commansd
def update_running_total_label(string_var):
  string_var.set('SUBTOTAL: ${}'.format(running_total))

#createing the receipt
def create_receipt():
    #write reciept_txt to file
    #print to console as well
    print(receipt_txt)
    return receipt_txt
    



