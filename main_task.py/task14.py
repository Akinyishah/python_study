# Write a program that takes input of 2 values and adds them. The program should only accept numbers and 
# floats only or otherwise display an error “invalid character entered” and
# take the user to re-enter the inputs .
#while TRUE-WORKS WITH TRY AND EXCEPT
while True:
    try:
        num1=float(input('enter your number: '))
        num2=float(input('enter your number: '))
        x=num1+num2
        print(x)
        break
    except:
        print('invalid character entered')

