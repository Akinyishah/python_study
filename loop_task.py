# 1.Write a program that displays a numbers 1 to 50 inside a list.
numbers=list(range(1,51))
print(numbers)

# 2.From 1 above display the ones divisible by 7 or 5 inside a list.
numbers=list(range(1,51))
divisible_5_7=[]           
for i in numbers:
    if i%5==0 or i%7==0:
        divisible_5_7.append(i) # HAVING THE.append to add values to list because its its not there the list will be empty

print( divisible_5_7)       

# 3.Find sum and average of values in the range between 10 to 40.
values=list(range(10,41)) #more we loop it increments original value when suming always have 0/TRY NOT TO USE SUM FUNCTION
total=0                   #when you start suming always have 0 then with each loop it will increment.
for i in values:          #i repsents each item
          total+=i
print(total)
avg=total/len(values)
print(avg)

# 4.Put in a list the first 10 odd numbers between 10 to 50. (for num in range(10,51))
oddnumbers=[]
count=0 # counting them if told to count and increase them with the count+=1-this will count upto the 10th one
for nums in range(10,52):
       if nums % 2==1:
              count+=1
              if count<=10:
                     oddnumbers.append(nums)
              else:
                     break
print(oddnumbers)              
              
# 5.write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
number=int(input('enter number: '))
for i in range(11):
     mult=number*i
     print(f"{number}*{i}={mult}") #Formatted string used to putting variables inside a string used by f""


# 6.write a program that counts and prints the number of even numbers between 1 and 50 using a for loop TEACH ME 
even_count=0 # or just count=0
for i in range(1,51):
      if i % 2==0:
            even_count+=1
print(even_count)
        
# 7.ls1 = [ (“Jay”, 20), (“Mo”, 30), (“Mya”, 32) ] REAL WORLD SCENARIO
# Display the total quantity of the 3 above.
ls1 = [ ('Jay', 20), ('Mo', 30), ('Mya', 32),('sha',200) ]
total=0 #having this if we want it count itself
for i in ls1:
      quantity=i[1]# storing the list of indexes in an iteration where it will add itself automatically
      total+=quantity #the total is where it starts counting 
print(total)      

