days=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

#ordered
print(days[0])
#slice
print(days[1:4])
print(type(days))

#immutable
#days[0]="MON" if it was alist can be mutated.
#1.convert to a list using list() function to convert tuple to list then modify
days=list(days)
print(type(days))

#modify
days[0]="mon"
print(days)
#after modifying your item convert it back to the tuple by using tuple() function
days=tuple(days)
print(days)
print(type(days))

data=("Python","java","C++","JavaScript")
#print the first and last statement
print(data[0])
print(data[-1])
#convert the tuple into a list add Go and convert it back 
data=list(data)
print(data)
print(type(data))
data.append("Go")
print(data)

#convert it back to tuple
data=tuple(data)
print(data)
print(type(data))



x=7%2
print(x)
y=14%2
print(y)