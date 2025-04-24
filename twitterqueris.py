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



2.#what is the value of X after executing the code
x=5
y=x  #y=5
x=x+2  #x=5+2 which will make x change into 7 
x += x+4 # same as  x = x + (x + 4).
# so x=7+(7+4)= 18 so x will change to 18 y will still remain 5

print(x)

#Meaning of +=
#The expression x += y is equivalent to x = x + y.
#It takes the current value of the variable x, adds the value of y to it, and then assigns the result back to x.

3.#Center the below text using 8 #
string='PYTHON'             #The original string ('PYTHON') has a length of 6.
result=string.center(8,'#') #The center() method is a built-in string method in Python that 
                            #centers the string within a specified width, padding it with a specified fill character 
                            # (or spaces by default).The desired width is 8, so there are 8 - 6 = 2 extra spaces to fill.
                            #The center() method places the string in the middle and distributes the padding evenly on both sides. 
                            #If the padding cannot be split evenly, the extra padding goes to the right.
print(result)

4.#can use dictionary in place of long if else statements in order to make code clean.
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


5.#The += operator adds the value of 2 * i to result and updates result in each iteration.
#range(5) generates numbers from 0 to 4 (end value is exclusive).
# The loop accumulates the sum of 2 * i for each i, starting from result = 0.
result=0 
for i in range(5):
    result+=2*i
print(result)    

6.#Reverse 987 to 789 without using an inbuilt -method or Assigning 789 manually.
#Hint: Strings can be reversed using [::-1]
#1,identify location of 987
#2.convert to a string
#3.now reverse the string and convert it back to INT
#my_ds[4]=int(str(my_ds[4])[::-1])- can also be used to change on 1 line

my_ds = [23,"Jane", (560), ["Lesson", "Maths",{"currency" : "KES"}], 987, (76,"John")]
my_ds[4]=str(my_ds[4])
my_ds[4]=my_ds[4][::-1]
my_ds[4]=int(my_ds[4])
print(my_ds)
print(type(my_ds[4]))
 