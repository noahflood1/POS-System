'''
For processing transactions
'''

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

def addToCartList(item, amount):
    #change the item parameter's amount in cart value to "amount"
    #add that item to cartList
    yup = UI_commands2.getItemFromList(item)
    yup.setCart(amount)

def update_running_total_update():
    # for every item in cartList, reset the running total to zero, incremember running total
    # by the amount of the item in cart times the price

    global running_total
    running_total = 0
    for item in cartList:
        item_X_amount_in_cart = (item.price * item.cart)
        running_total += item_X_amount_in_cart

#function that updates the running total on screen? do how you did it with update_inventroy list function in UI commansd
def update_running_total_label():
    pass

#createing the receipt
def create_receipt():
    print(receipt_txt)
    return receipt_txt
    



