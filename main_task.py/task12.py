# Write a program that prints the largest of 4 inputs taken as input from a user.
# user1=int(input('enter your marks: '))
# user2=int(input('enter your marks: '))
# user3=int(input('enter your marks: '))
# user4=int(input('enter your marks '))
user1=float(input('enter your marks: '))
user2=float(input('enter your marks: '))
user3=float(input('enter your marks: '))
user4=float(input('enter your marks '))

def four_largest(user1,user2,user3,user4):
    if user1>user2 and user1>user3 and user1>user4:
         print(f'{user1} is the largest') #can use a formated string print(f'[person 1}is the largest)
    elif user2>user1 and user2>user3 and user2>user4: 
           print(f'{user2} is the largest')
    elif user3>user1 and user3>user2 and user3>user4:
         print(f'{user3} is the largest')       
    else:   
          print(f'{user4} is the largest')
         
four_largest(user1,user2,user3,user4)    





 