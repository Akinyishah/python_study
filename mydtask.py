#my_ds = [23, “Jane”, (560), [“Lesson”, “Maths”, {“currency” : “KES”}], 987, (76,”John”)]
my_ds = [23,"Jane", (560), ["Lesson", "Maths",{"currency" : "KES"}], 987, (76,"John")]

#1. Print KES
print(my_ds[3][2]['currency'])

#2. Print 560
print(my_ds[2])

#3. Print Maths
print(my_ds[3][1])

#4. In the dictionary with the key currency, add another key “amount” with value 90
#my_ds[3][2]["amount"]=90 / can be used to add a new key on the dictionary
my_ds[3][2].update({'amount':90,'mode':'Visa'})
print(my_ds)

#5.Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually.
#Hint: Strings can be reversed using [::]
#1,identify location of 987
#2.convert to a string
#3.now reverse the string and convert it back to INT
#my_ds[4]=int(str(my_ds[4])[::-1])- can also be used to change on 1 line
my_ds[4]=str(my_ds[4])
my_ds[4]=my_ds[4][::-1]
my_ds[4]=int(my_ds[4])
print(my_ds)
print(type(my_ds[4]))

#6. Change the name “John” to “Jane” .
# Convert the tuple to a list
#locate John
print(my_ds[5])
#convert it to a list
my_ds[5]=list(my_ds[5]) 
#modify
my_ds[5][-1]='jane'
#convert back to a tuple 
my_ds[5]=tuple(my_ds[5])
print(my_ds)
print(type(my_ds[5]))
















