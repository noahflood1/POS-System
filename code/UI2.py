'''
Program for outputting the actual User Interface with all of it's functions

@authors: 
Noah Flood
Jackson S.
'''

from tkinter import *
from tkinter.font import Font
from random import *
from code import UI_commands2

def mainWin(): #Defines UI in terms of a window with widgets

  #loads/initalizes the inventory list based on a csv file
  UI_commands2.load_list()

  #----------------------------------------------------
  #starts main window loop as "win"
  win=Tk() 
  win.title('POS system')

  #geometry of the main window
  window_height = 1024
  window_width = 768
  win.geometry("{}x{}".format(window_height, window_width))
  win.config(bg='black')
  
  #contrict the size of window so that it can't be resized
  win.minsize(window_height, window_width)
  win.maxsize(window_height, window_width)
  
  #allows for things to be placed in window using grid, not sure why
  win.rowconfigure(0, weight=1)
  win.columnconfigure(0, weight=1)

  '''
  Visual formatting for the program is currently made for MacOS.
  '''


  #----------------------------------------------------
  #define fonts to stylize text

  #title Font
  title_font = Font(
      family="Helvetica",
      size= 30,
      weight='bold'
      )
  
  #font fot menu label
  big_font = Font(
    family="Helvetica",
    size=25,
    weight='bold'
  )

  #font for buttons  font=button_font
  button_font = Font(
    family="Helvetica",
    size=18,
  )

  #font for the plain text within the program font=text_font_2
  text_font_2 = Font(
    family='Helvetica',
    size=20,
    weight='bold'
  )

  #----------------------------------------------------
  #Code for all the windows creation and packing

  #Define frames that are the different "screens"
  main_frame = Frame(win)
  inventory_frame = Frame(win)
  add_delete_frame = Frame(win)
  stocks_frame = Frame(win)
  transaction_frame = Frame(win)
  restock_frame = Frame(win)

  #FIXME: Add all new frames into this loop so that they exist in the window
  #They all exist on top of one another simultaneously, but only one is showing at a time (only one is on top at a time)
  #TASKS DONE FOR ALL THE WINDOWS##############################
  for frame in (main_frame, inventory_frame, add_delete_frame, stocks_frame, transaction_frame, restock_frame):

    frame.grid(row=0, column=0, stick='nsew') #does grid() to all these frames. only the last one grided shows; this is fixed with the function show_frame() below

    if not(frame == main_frame):
      #create and add a back button to the frame
      back_button = Button(frame, font=button_font, text='Back', command=lambda:UI_commands2.show_frame(main_frame), background="black", fg='white', height=2, width=10)
      back_button.place(x=800, y=400) #FIXME: Change this to a normal coordinate


  #----------------------------------------------------
  #main_frame code
  #title label
  titleLabel = Label(main_frame, text='POS System', bg='#4dd2ff', fg='black', font=title_font)
  titleLabel.pack(fill='x', ipady='10', pady='10')

  #menu label
  myLabel = Label(main_frame, text="Menu:", font=big_font)
  myLabel.pack(pady = 10)

  #inventory button
  btn1 = Button(main_frame, text='Inventory', command=lambda:UI_commands2.show_frame(inventory_frame), background="black", fg='white', height=2, width=10, font=button_font)
  btn1.pack(pady=10)

  #button to add/delete items (previously: button command=addWindow ANDD another button whose command == delWindow)
  btn2 = Button(main_frame, text='Add/Delete Items', command=lambda:UI_commands2.show_frame(add_delete_frame), background="black", fg='white', height=2, width=13, font=button_font)
  btn2.pack(pady=10)

  #button for transaction screen
  btn3 = Button(main_frame, text='Transaction', command=lambda:UI_commands2.show_frame(transaction_frame), background="black", fg='white', height=2, width=10, font=button_font)
  btn3.pack(pady=10)

  #button for restock screen
  btn4 = Button(main_frame, text='Restock',command=lambda:UI_commands2.show_frame(restock_frame), background="black", fg='white', height=2, width=10, font=button_font)
  btn4.pack(pady=10)

  #button to quit the program
  quitButton = Button(main_frame, font=button_font, text='Quit', command=lambda:quit(win), background="black", fg='white', height=2, width=10)
  quitButton.place(x=800, y=660)





  '''
  'MAIN' code to work on-------------------------------------------------------------------------------------------------------------------------------------
  '''





  #----------------------------------------------------
  #inventory_frame code
  #header label
  inventory_header = Label(inventory_frame, text='Inventory', bg='#4dd2ff', fg='black', font=title_font)
  inventory_header.pack(fill='x', ipady='10', pady='10')

  #label for list
  description_label = Label(inventory_frame, text='Name-----Amount-----Price', font=text_font_2)
  description_label.pack()

  #get an inventory list object and pack it into this frame
  inventory_listbox = UI_commands2.getFramedInventoryList(inventory_frame)
  inventory_listbox.pack()

  #when the button is clicked, we print inventory in terminal for testing
  print_inventory_button = Button(inventory_frame, font=button_font, text="Print Inventory", command=lambda:UI_commands2.printInventoryList(), background="black", fg='white', height=2, width=10)
  print_inventory_button.place(x=800, y=100)

  #when the button is clicked, we update the list based upon the inventoryList list object
  update_list_button = Button(inventory_frame, font=button_font, text="Update List", command=lambda:UI_commands2.updateFramedInventoryList(inventory_listbox), background="black", fg='white', height=2, width=10)
  update_list_button.place(x=800, y=160)


  #----------------------------------------------------
  #add_delete_frame code
  #header label
  add_delete_header = Label(add_delete_frame, text='Add/Delete Items', bg='#4dd2ff', fg='black', font=title_font)
  add_delete_header.pack(fill='x', ipady='10', pady='10')

  #write instructions
  instructions1 = Label(add_delete_frame, font=text_font_2, text="Enter item name, amount, and price.\nPress button to add to the inventory list.")
  instructions1.pack()

  #create three entry forms to get information for the new item, pack all three
  name_entry = Entry(add_delete_frame, width=20, font=text_font_2)
  name_entry.pack()
  amount_entry = Entry(add_delete_frame, width=20,font=text_font_2)
  amount_entry.pack()
  price_entry = Entry(add_delete_frame, width=20, font=text_font_2)
  price_entry.pack()

  #clears the text from each of the add entry fields
  def clearAddEntry():
    name_entry.delete(0, END)
    amount_entry.delete(0, END)
    price_entry.delete(0, END)

  #actually get the values from the three entries and store in variables using function
  #returns a list of the parameters
  def getNewItemParameters():
    new_name = name_entry.get()
    new_amount = amount_entry.get()
    new_price = price_entry.get()
    return [new_name, new_amount, new_price]

  #create a button with a command that WHEN PRESSED, connects to TWO FUCNTIONS function that:
                                        #1) takes three parameters (as a list)to use to instantiate a new Item object which is then added to the inventoryList 
                                        #2) updates the file with the inventoryList afterwards
  add_button = Button(add_delete_frame, text='Add', font=button_font, command=lambda:(UI_commands2.addToInventoryList(getNewItemParameters()), UI_commands2.update_file(), clearAddEntry()), background="black", fg='white', height=2, width=10)
  add_button.pack()

  #delete instructions
  instructions2 = Label(add_delete_frame, font=text_font_2, text="Enter name of the item to delete.\nPress button to delete from the inventory list.")
  instructions2.pack()

  #Delete entry box
  del_entry = Entry(add_delete_frame, width=20)
  del_entry.pack()

  #cleares the delete entry field
  def clearDeleteEntry():
    del_entry.delete(0, END)

  delButton = Button(add_delete_frame, font=button_font, text='Delete', command=lambda:(UI_commands2.deleteFromInventoryList(del_entry.get()), UI_commands2.update_file(), clearDeleteEntry()), background="black", fg='white', height=2, width=10)
  delButton.pack()

  #----------------------------------------------------
  #transaction screen frame code
  transaction_header = Label(transaction_frame, text='Transaction', bg='#4dd2ff', fg='black', font=title_font)
  transaction_header.pack(fill='x', ipady='10', pady='10')

  #tempory label for this screen
  transaction_label_temp = Label(transaction_frame, font=text_font_2, text='Welcome. Enter items you would like to buy and the amount of each.')
  transaction_label_temp.pack(pady=10)

  #field for item name
  itemEntry = Entry(transaction_frame, width=20, font=text_font_2)
  itemEntry.pack()

  #field for amount of item wanted
  amountEntry = Entry(transaction_frame, width=20, font=text_font_2)
  amountEntry.pack()

  #FIXME command for this button
  #Button to add an item's price to the total
  addButton = Button(transaction_frame, text='Add to Cart', font=button_font, command=lambda:UI_commands2.show_frame(main_frame), background="black", fg='white', height=2, width=10)
  addButton.pack()

  #FIXME command for this button 
  #Button to go through with the transaction
  transaction_button = Button(transaction_frame, text='Confirm', font=button_font, command=lambda:UI_commands2.show_frame(main_frame), background="black", fg='white', height=2, width=10)
  transaction_button.pack()

  #Button to go back
  back_button_transaction = Button(transaction_frame, text='Back', font=button_font, command=lambda:UI_commands2.show_frame(main_frame), background="black", fg='white', height=2, width=10)
  back_button_transaction.place(x=800, y=660)


  

  #-----------------------------------------------------
  #Restock Frame Code

  restockHeader = Label(restock_frame, text='Restock', bg='#4dd2ff', fg='black', font=title_font)
  restockHeader.pack(fill='x', ipady='10', pady='10')

  restockLabel = Label(restock_frame, font=text_font_2, text='Item Name')
  restockLabel.pack()
  itemName = Entry(restock_frame, width=20)

  #Labels and entry fields for restock
  #I know it looks bad, but it works
  quantityLabel = Label(restock_frame, font=text_font_2, text='Quantity of Item')
  quantity = Entry(restock_frame, width=20)
  dayLabel = Label(restock_frame, font=text_font_2, text='Day')
  day = Entry(restock_frame, width=20)
  monthLabel = Label(restock_frame, font=text_font_2, text='Month')
  month= Entry(restock_frame, width=20)
  yearLabel = Label(restock_frame, font=text_font_2, text='Year')
  year= Entry(restock_frame, width=20)
  itemName.pack()
  quantityLabel.pack()
  quantity.pack()
  dayLabel.pack()
  day.pack()
  monthLabel.pack()
  month.pack()
  yearLabel.pack()
  year.pack()

  def clearRestock():
    itemName.delete(0, END)
    quantity.delete(0, END)
    month.delete(0, END)
    year.delete(0, END)
    day.delete(0, END)
  #restocks an item based off of 4 parameters
  #Quantity to restock
  restockButton = Button(restock_frame, text='Restock Item', font=button_font, command=lambda:(UI_commands2.restock(itemName.get(),quantity.get(),month.get(),year.get(),day.get()), clearRestock() ), background="black", fg='white', height=2, width=10)
  restockButton.pack()


  #-----------------------------------------------------
  #show the main frame on top first
  UI_commands2.show_frame(main_frame) #we want to start out seeing the title screen


#----------------------------------------------------
#All GUI functions occur between these two lines
mainWin()
mainloop()