#1.Assume start_date = '2024-01-01' and end_date = '2024-12-31'.
# Write a conditional statement that checks:
#If start_date comes before end_date, print "Valid period",
#If start_date is after end_date, print "Invalid period".
#If both dates are the same, print "One-day period".
# from datetime import datetime
start_date='2022-01-01'#2022 which is start date comes before end date it will be valid period
end_date='2023-01-01'
# date_format='%Y-%m-%d'
# validity=''
# start_date = datetime.strptime(start_datestr, '%Y-%m-%d')
# end_date = datetime.strptime(end_datestr, '%Y-%m-%d')
if start_date<end_date:
    validity='Valid period'
elif start_date>end_date:
    validity='Invalid period'  
else:
    validity='One-day period'
print(validity)


#2.Given two strings str1 and str2, write a conditional statement that checks:
#If str1 is longer than str2, print "str1 is longer".
#If str2 is longer than str1, print "str2 is longer".
#If both have equal length, print "Both are of equal length".
str_1='strawberries'
str_2='bananasssssssss'
if len(str_1) > len(str_2):
    print('str1 is longer')
elif len(str_2) > len(str_1):
    print('str2 is longer')      
else: 
     print('Both are of equal length') 

#3.Given a list valid_ids = [101, 102, 103] and a variable user_id = 105, 
# write a conditional statement that:
#Prints "Access Granted" if user_id is in valid_ids.
#Prints "Access Denied" if user_id is not in valid_ids.
user_id=105
valid_ids=[101,102,103]
res=''
if user_id in valid_ids:
    res='Access granted'
else:
    res='Access denied'        
print(res)

#4.Given a variable value that could be of any type, write a conditional statement that:
#Prints "String Detected" if value is a string.
#Prints "Integer Detected" if value is an integer.
#Prints "Unknown Type" for any other type. CHECK CODE.#isinstance checks whether an item is of a specified class, 
#looking for the type of the value.    
value=1000.50
#print(type(value))
if type(value)==str:
    datatype=('string detected')
elif type(value)==int:
    datatype=('Interger Detected')
else:
    datatype=('unknown type')
print(datatype)            


#5.Given x = 7 and y = 14, write nested conditional statements that print:
#"x and y are both even" if both x and y are even numbers.
#Only y is even" if only y is even.
#"Neither x nor y are even" if both are odd./can do without nested 
x=20
y=14
if x%2==0 or y%2==0:
    if y%2==0 and x%2==0:
         num_type='x and y are both even'
    elif y%2==0:
        num_type='Only y is even'
    else:
        num_type='Only x is even'
else:
    num_type='either x nor y are even'  
      
print(num_type)           

    
               

         


 
 



 




