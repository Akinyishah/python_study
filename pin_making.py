# take input from the user print
# compare it with the correct pin 1234
# if correct print welcome
# otherwise we print account blockedafter giving 3 attempts 
# oe each attempt inform the user the number of remaining attempts 
correct_pin='7151'
attempts=3
for i in range(1,4): #with this it will count the 3 attempts needed for the pin
    pin=(input('enter your pin: '))
    if pin==correct_pin:
        print('welcome')
        break
    else:
        remaining_attempts=attempts-i
        if remaining_attempts>0:
            print(f'wrong pin you have {remaining_attempts} attempts remaining')
        else:
            print('account blocked')    