# create a programs that acts like like a stock, randomly changes price perodically
import random
import datetime 

date=[]
openprice=[]

def prices():
  begin = datetime.date(2021, 1, 1)
  end = datetime.date(2021, 12, 31)
  start= random.uniform(.1, 2.5)
  next_day = begin

  t=[]
  openlist=[]
  while True:
    if next_day > end:
        break
    days=[]
    while len(days)<1:
        price = float(start) + random.uniform(-.1,.1)
        days.append(round(price, 2))
        open= days[0]
        t.append(str(next_day))
        openlist.append(open)
        next_day += datetime.timedelta(days=1)
    global date 
    date= t
    global openprice
    openprice= openlist

prices()

restock={'date':'price'}
count=0
for thing in date:     
    restock[thing]= openprice[count]
    count+=1

