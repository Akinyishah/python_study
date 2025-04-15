# Write a program that calculates the total stock in a company from the array/list below if we know 
# that the stock is the last digit in every array/list.

prods = [['omo','30kshs','300'],
         ['milk','50kshs','200'],
         ['bread','45kshs','359'],
         ['coffee','5kshs','79']]
for p in prods:
         p[-1] = int(p[-1])
print(prods)
total_stocks=0  #having this if we want it count itself from 1 item/element to the next.
for p in prods:
        quantity=p[-1]
        total_stocks+=quantity        
print(total_stocks)
        



# def total_stockscheck(STOCKS):
#     for p in prods:
#          p[-1] = int(p[-1])
#          print(prods)
# total=0  #having this if we want it count itself from 1 list to the next.
# for p in prods:
#       quantity=p[-1]
# total+=quantity
# total_stockscheck()





   





































#        ls1 = [ ('Jay', 20), ('Mo', 30), ('Mya', 32),('sha',200) ]
# total=0 #having this if we want it count itself
# for i in ls1:
#       quantity=i[1]# storing the list of indexes in an iteration where it will add itself automatically
#       total+=quantity #the total is where it starts counting 
# print(total)      




















