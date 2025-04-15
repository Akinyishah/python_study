# Write a program which accepts email as form input or from terminal. 
# Validate the email by checking if it's a valid email. 
# Hint: Check if it contains an “@” symbol and “.” symbol.
# email=input('enter your email: ')
# if '@'in email and '.' in email: #checking if the symbols exists on the provided email.use the membership IN
#     print('valid email')
# else:
#     print('invalid email')    

def email_check(email):
    email=input('enter your email: ')
    if '@' in email and '.' in email:
        print('valid email')
    else:
        print('invalid email')
email_check('email')
    
          
































