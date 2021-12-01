'''
For processing transactions
'''
import tkinter as tk
from code import UI_commands2

#Filepath for reciept
filepath = "files/reciept.txt"

#global variable about store
business_title = "Grandma's Bakery"
business_phone = "256-420-6969"

def setNum():
    global receipt_num
    f = open('files/num.txt','r')
    receipt_num = int(f.read())
    f.close()



#variables for person using POS
customer_name = "Customer"
location = 'Auburn AL'
receipt_num = 0
setNum()
receipt_header = str(receipt_num) + ' - ' + location

#cart stuff
cartList = []

#variables for receipt
receipt_txt = "Test"
running_total = 0
subtotal = 0
total = 0
tax = 0.09

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
    global subtotal
    tempvar = 0
    for item in cartList:
        #print(item.name, item.stock, item.price, item.cart, 'CARTLIST')

        item_X_amount_in_cart = (float(item.price) * float(item.cart))
        tempvar += float(item_X_amount_in_cart)
    running_total = tempvar
    subtotal = running_total

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

#writes receipt from cartList
#INCREMENT THE RECIEPT NUBMER A TTHE END
#item_text = "{name:<15}{stock:<5}{price:>6}".format(name=item.name, stock=item.stock, price=item.price)
def write_receipt():
    #Each line will be 42 Chars in total 
    #print(cartList)
    global receipt_txt
    global receipt_num
    receipt_txt = '='*42 + '\n'
    receipt_txt += "{a:^42}".format(a='#'+receipt_header) + '\n'
    receipt_txt += "{a:^42}".format(a='--'+business_title+'--') + '\n'
    receipt_txt += "{a:^42}".format(a=business_phone) + '\n'
    receipt_txt +=  '\n'
    receipt_txt += '-'*42 + '\n'
    receipt_txt += "{a:<18}{b:<8}{c:>5}{d:>11}".format(a='Item',b='Qty',c='Price',d='Total') + '\n'
    receipt_txt += '-'*42 + '\n'
    for item in cartList:
       if(item.cart != 0):
            total = float(item.price) * int(item.cart)
            receipt_txt += "{a:<18}{b:<8}{c:>5}{d:>11}".format(a=item.name,b=item.cart,c=item.price,d=total) + '\n'
    receipt_txt += "{a:>42}".format(a='-'*12) + '\n'
    receipt_txt += "{a:<21}{b:>21}".format(a='Subtotal',b='$'+str(round(subtotal,2))) + '\n'
    receipt_txt += "{a:<21}{b:>21}".format(a='Tax',b='$'+str(round(subtotal*tax,2))) + '\n'
    receipt_txt += "{a:>42}".format(a='-'*12) + '\n'
    receipt_txt += "{a:<21}{b:>21}".format(a='Total',b='$'+str(round(subtotal+(subtotal*tax),2))) + '\n'
    receipt_txt += "{a:>42}".format(a='~'*12) + '\n'
    receipt_txt += "{a:<42}".format(a='Tender:') + '\n'
    receipt_txt += "{a:<21}{b:>21}".format(a='Debit',b='$'+str(round(subtotal+(subtotal*tax),2))) + '\n'
    receipt_txt += "{a:<42}".format(a='*'*12 + '8008') + '\n'
    receipt_txt += '='*42 + '\n'

    receipt_num +=1
    f = open('files/num.txt','w')
    f.write(str(receipt_num))
    f.close()
    setNum()
    create_receipt()    

#createing the receipt
def create_receipt():
    #write reciept_txt to file
    print(receipt_txt)
    f = open(filepath,'w')
    f.write(receipt_txt)
    f.close()
    #print to console as well
    return receipt_txt
    



