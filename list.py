fruits= ['oranges','grapes','cherry','pineapple','apple']
print(type(fruits))#list
print(fruits[0])
print(fruits[-2])
# using index to change 
fruits[-1]='kiwi'
print(fruits)
#slicing
y=fruits[1:4+1]
print(y)
print(fruits[1][0].capitalize())


#nested list
mylist=['a','b','c','d',[1,2,3,[10,20,30,40],4,6]]
print(mylist[4][3][2])
print(mylist[4][3])