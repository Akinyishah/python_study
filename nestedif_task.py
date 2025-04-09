#Write a program that:
#Takes a transaction amount and account type ("Standard" or "Premium") as input.
#If the account type is "Standard":
#Check if the amount is above 500:
#If it is, print "Transaction exceeds the limit for Standard accounts."
#If not, print "Transaction approved."
#If the account type is "Premium":
#Check if the amount is above 1,000:
#If it is, print "Transaction exceeds the limit for Premium accounts."
#If not, print "Transaction approved."

transaction_amount=float(input('enter your amount ')) 
account_type=input('enter your account type "Standard" or "Premium" ').casefold()
respond=''
if account_type=='Standard':
    if transaction_amount>500:
        respond='Transaction exceeds the limit for Standard accounts'
    else:
        respond='Transaction approved'
elif account_type=='Premium':
    if transaction_amount>1000:  
         respond='Transaction exceeds the limit for Premium account'
    else:
        respond='Transaction approved'    
else:
    respond='wrong account type '                    
print(respond)        




                  

           



















