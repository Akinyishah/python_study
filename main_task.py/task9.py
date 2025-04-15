# Write a program called stars. It should prompt the user for a number, 
# and it should print the number of stars till the number entered.
# Example If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****.....
def stars():
        stars=int(input('enter your number of required stars: '))
        for i in range(1, stars+1): #starts counting from 1 upto to where the value of stars i where it will stop
                                    #.because our astericks are counting from 1 +1 is to include the exact value inputted 
                  print('*' * i)                                                     
stars()                        















  






















































































# # 5.write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
# number=int(input('enter number: '))
# for i in range(11):
#      mult=number*i
#      print(f"{number}*{i}={mult}") #Formatted string used to putting variables inside a string used by f""