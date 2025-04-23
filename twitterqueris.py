1.#given a list of strings,write a python function  that returns a dictionary where the keys are the strings 
# and the values are the number of times each string appears in the list for example the list above 
# should out put {'apple':2,'banana':1,'Cherry':1}
fruits=['apple','banana','apple','cherry'] # list of fruits containg 4 strings of elements
fruit_count={} # empty dictionary that will be used to store the count of each fruit
for i in fruits: # for loop that iretares over each element
    if i in fruit_count: #This checks if the current fruit (i) is already a key in the fruit_count dictionary.
        fruit_count[i] +=1 #If i is a key, the code executes fruit_count [i] += 1, which increments the value associated with that key by 1 (i.e., increases the count of that fruit).
    else:
        fruit_count[i]=1 #If i is not a key in the dictionary, the code executes fruit_count [i] = 1, which adds the fruit as a new key to the dictionary with an initial value of 1 (indicating it’s been seen once).
print(fruit_count)   


# MORE PRECISE WAYS OF DOING THE ABOVE QUERY.USING COLLECTIONS.COUNTER read more on this 
from collections import Counter
fruits=['apple','banana','apple','cherry']
fruit_count=Counter(fruits)
print(dict(fruit_count))



#what is the value of X after executing the code
x=5
y=x  #y=5
x=x+2  #x=5+2 which will make x change into 7 
x += x+4 # same as  x = x + (x + 4).
# so x=7+(7+4)= 18 so x will change to 18 y will still remain 5

print(x)

#Meaning of +=
#The expression x += y is equivalent to x = x + y.
#It takes the current value of the variable x, adds the value of y to it, and then assigns the result back to x.


string='PYTHON'             #The original string ('PYTHON') has a length of 6.
result=string.center(8,'#') #The center() method is a built-in string method in Python that 
                            #centers the string within a specified width, padding it with a specified fill character 
                            # (or spaces by default).The desired width is 8, so there are 8 - 6 = 2 extra spaces to fill.
                            #The center() method places the string in the middle and distributes the padding evenly on both sides. 
                            #If the padding cannot be split evenly, the extra padding goes to the right.
print(result)

#can use dictionary in place of long if else statements in order to make code clean.
food_item=input('enter foor item Name: ')
food_items_dict={
    "Burger":100,
    "pizza":200,
    "juice":50,
    "Tofu":150
}
def getprice(food_item):
    return food_items_dict.get(food_item,0)
print(getprice(food_item))


result=0 #The += operator adds the value of 2 * i to result and updates result in each iteration.
for i in range(5):#range(5) generates numbers from 0 to 4 (end value is exclusive).The loop accumulates the sum of 2 * i for each i, starting from result = 0.
    result+=2*i
print(result)    
 