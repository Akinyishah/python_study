#1.Take three inputs from a user, separately. Print the largest of the numbers.
    #Hint: Determine what type of data is taken in as input.
user1=int(input('enter your marks: '))
user2=int(input('enter your marks: '))
user3=int(input('enter your marks: '))
user4=int(input('enter your marks '))
if user1>user2 and user1>user3 and user1>user4:
    print(user1,'is the largest number ')  
elif user2>user1 and user2>user3 and user2>user4:
    print(user2, 'is the largest number')  
elif user3>user1 and user3>user2 and user3>user4:
    print(user3, 'is the largest number')        
else:
    print(user4,'is the largest number')    

#2.Take as input from a user the temperature if the temperature is above 30°C 
#display “The temperature is too high”,if the temperature is above 15 display
#“Normal temperature” otherwise display “Cold temperature”
temp=input('enter the temperature in °C:')
temp=float(temp)
if temp >=30: 
    print('The temperature is too high')
elif (temp>=15) and temp<30:
    print('Normal temperature')    
else:
    print('Cold temperature')    

#3.Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
#and if another variable y is greater than 100. If both conditions are true,
#print "Conditions met", otherwise print "Conditions not met"
x=int(input('enter the value x: '))
y=int(input('enter the value y: '))
#if 10>=x<20x
if x>=10 and x<=20 and y>100:
    print('Conditions met')
else:
    print('Conditions not met')    

#4.Write a Python program that checks if a variable password is equal
#to the string "secret123". and a variable email is equal to"admin@gmail.com" If it is, print "Access   granted", otherwise print "Access denied"
password=input('enter password: ')
email=input('enter email: ')
correct_password='secret123'
correct_email='admin@gmail.com'
if password==correct_password and email==correct_email:
    print('Access granted')
else:
    print('Access denied')    

#5.Write a Python program that checks if a variable student_score is greater than 90. 
# If true, check if the attendance is greater than 80. If both conditions are true, 
# print "Excellent student", otherwise print "Good score,
 #but attendance needs improvement"- when you see if true it becomes a nested IF
 #learn to store variables e.g the results 
student_score=input('enter score: ')
result=''
student_score=int(student_score)
if student_score>=90: #always confirm the score first
    attendance=input('enter attendance: ')
    if  attendance>=80:    
        results=('Excellent student')
    else:
          results=('Good score,but attendance needs improvement')
else:
    results=('bad score')   
print(results)           




  