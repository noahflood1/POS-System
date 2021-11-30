from code import Restock as r

#pull product prices and proccess customer transactions

total= 0

#dictionary {ItemName:amountBought}
#  tempDict={}
#  count=0
#  for item in itemList:
#    tempDict.update({item.name:count})
#    count+=1
#  tempDict.get(name)
#--------------------------------------------

# create a 'bank account' for owner
class Bank_Account:
    def __init__(self):
        self.balance=1000

    def deposit(self):
        amount=total
        self.balance += amount
 
    def withdraw(self, funds):
        amount = float(funds)
        if self.balance>=amount:
            self.balance-=amount
            return(True)
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
            return(False)
 
    def display(self):
        print("\n Net Available Balance=",self.balance)
# Driver code
  
# creating an object of class
global s
s = Bank_Account()


#pull restock prices for Owner and process their transactions
def restockDate(quanity,month,year,day):
  q=str(year)+'-'+ str(month)+ '-'+  str(day)
  funds=float(r.restock[str(q)])*float(quanity)
  return(s.withdraw(funds))