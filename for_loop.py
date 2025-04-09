x=[10,20,30,40,50,60]
for num in x:
    print(num)
#create a list of numbers from 1 t0 100- use the range()-function use the list function
numbers=list(range(1,101))
print(numbers)
for i in numbers:
    print(i)

#display even numbers bewteen 100 and 200,bring in the conditional statement to make a decison
mynumbers=list(range(100,200))
for num in mynumbers:
    if num%2==0:
        print(num)
        
#display numbers divisible by 5 between 50 and 150
numbers=list(range(50,150))
divisible_5=[] #declare a variable and give blank list and append the i variable to have everything inside that list.
for i in numbers:
    if i%5==0:
        divisible_5.append(i)
print(divisible_5)


#store in a list odd numbers from 1 to 50 stop at 35
my_numbers=list(range(1,51))
oddnumbers=[]
for i in my_numbers:
    if 1==36:
        break #stops loop
    if i%2!=0: #to get odd numbers
        oddnumbers.append(i)
print(oddnumbers)        



