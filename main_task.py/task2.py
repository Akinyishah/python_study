# Prompt the user for a number either on a form input or the terminal. Depending on 
# whether the number is even or odd, display  either “odd” or “even” to the user.
# Hint: how does an even / odd number react differently when divided by 2?
#WITHOUT FUNCTIONS 
# number=int(input('enter your number: '))
# if number % 2==0:
#     print('even')
# else:
#     print('odd')
# #Using the Functions:

# this is for when user has been told to input number 
def check_even_odd(number):
    if number % 2==0:
        print('even')
    else:
        print('odd')    
num=int(input('enter number: '))
check_even_odd(num)

 
#If the number is a multiple of 4, print out “divisible by 4”.