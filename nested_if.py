#1.write a program that takes users age as input
# if the age is 18 and above ,check if they have  drivers license if they do we print you are eligible to drive
# if they dont have a drivers license print you are not eligible to drive
# otherwise you are too young to drive
age=int(input('enter your age: '))
if age>=18:
    license=input('do you have a drivers license yes/no: ').lower
    if license=='yes':
        print('you are eligible to drive')
    else:
        print('you are not eligible to drive')    
else:
    print('you are too young to drive')        
 #1.Write a program that:
#Takes the user's credit score and annual income as input.
#If the credit score is above 700, check if the income is above 50,000:
#If both conditions are met, print "Loan approved."
#If only the credit score is high, print "Income requirement not met."    
credit_score=int(input('enter your credit score: '))
if credit_score>700:
    annual_income=float(input('enter your annual income: '))
    if annual_income>50000:
        res='Loan approved'
    else:
        res='Income requirement not met'
else:
    res='credit score too low'
  
print(res)            
 #1.Write a program that:
#Takes the user's credit score and annual income as input.
#If the credit score is below 700, check if the income is above 50,000:
#If both conditions are met, print "Loan approved."
#If only the credit score is high, print "Income requirement not met." 
credit_score=int(input('enter your credit score: '))
if credit_score<700:
      res='credit score too low'
else:
    annual_income=float(input('enter your annual income: '))
    if annual_income>50000:
        res='Loan approved'
    else:
        res='Income requirement not met'
print(res)       

















if student_score>=90: #always confirm the score first
    attendance=input('enter attendance: ')
    if  attendance>=80:    
        results=('Excellent student')
    else:
          results=('Good score,but attendance needs improvement')
else:
    results=('bad score')   
print(results)           