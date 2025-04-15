# Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores them in three variables.
#  Return the largest of the three. Do this without using the the inbuilt max () function!
# The goal of this exercise is to think about some internals that programs normally take care of for us. 
#
# user1=int(input('enter your marks: '))
# user2=int(input('enter your marks: '))
# user3=int(input('enter your marks: '))
# user4=int(input('enter your marks '))
# if user1>user2 and user1>user3 and user1>user4:
#     print(user1,'is the largest number ')  
# elif user2>user1 and user2>user3 and user2>user4:
#     print(user2, 'is the largest number')          
# else:
   # print(user3,'is the largest number')    
# person1=int(input('enter your marks: '))
# person2=int(input('enter your marks: '))
# person3=int(input('enter your marks: '))

def largestof_thethree(person1,person2,person3):
    notes='is the largest'
    if person1>person2 and person1>person2:
         return f'person1 {notes}'        #can use a formated string print(f'[person 1}is the largest)
    elif person2>person1 and person2>person3: 
         return f'person2 {notes}'
    else:   
         return f'person3 {notes}'
         
p1=int(input('enter num1: '))
p2=int(input('enter num2: '))
p3=int(input('enter num3: '))

x=largestof_thethree(p1,p2,p3)       #for such ensure to create a variable.
print(x)




# #store the function in a variable then print 
# x=largestof_thethree(100,63,30)  
# print(x)















