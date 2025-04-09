days={"monday","tuesday","wednesday","thursday", "friday","saturday","sunday","sunday","sunday","sunday"}
print(days)

fruits={"Grapes","Oranges","Kiwi","Lemon","Berries","Mango"}
#Adding an item inside a set, we can only add 1 item 
fruits.add("banana")
print(type(fruits))

#deleting items in a set
#remove- will give an error if the item does not exist,discard-Will ignore the element that does not exist will not give error 
fruits.remove("Oranges")
print(fruits)
fruits.pop()
print(fruits)

#SET OPERATIONS
set1={1,2,3,4,5,6,7,10,11}
set2={10,11,12,13,14,15}

set3=set1|set2 #(|) combines elements in the 2 sets 
print(set3)
set4=set1&set2 #(&) returns items that are common in both sets
print(set4)

set5=set1-set2 #(-) returns item in the first set that are not in the second set
print(set5)

set6=set1^set2 #(^) returns elements that are in either set but not in both sets 
print(set6)

s={'b', 'a', 'r'} & set('qux')
print(s)
sd={1, 2, 3, 4, 5} - {3, 4} ^ {5, 6, 7}
print(sd)

