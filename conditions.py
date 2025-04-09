age=10

if age>=18:
    print('you are an adult')
else:
    print('you are a minor')    


#write a program that checks if a number is positive, 
# if it is print positive number otherwise print not a positive
number=15
if number>=0:
    print('positive')
else:
    print('not a positive')    

#write a program that asks the user to enter their age if the age is 18 or above print access granted 
# otherwise print access denied
age=input("enter your age: ")
age=int(age)
if age>=18:
    print('Access granted')
else:
    print('Acess denied')    

#Grading System
marks=90
marks=input('enter your marks: ')
marks=int(marks)
if marks>=80:
    print('A')
elif (marks>=70) and marks<80:
    print('B')    
elif (marks>=60) and marks<70:
    print('C')    
elif(marks>=50) and marks<60:
    print('D')    
else:
    print('E')    
