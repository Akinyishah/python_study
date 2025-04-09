#create a list with five of your favourite things (movies,songs,food,e,t.c) print the first and last item
favs=['mission imposible','country music','lamb','missionblue','tattos']
print(favs[0])
print(favs[-1])

#given colors ["red","blue","green","yellow","purple"] print the second element,print the last 3 elements using slicing
colors=['red','blue','green','yellow','purple']
print(colors[1])
#slicing
z=colors[2:]
print(z)


#start with numbers =[2,4,6,8],change the second element to 10, add 12 at the end and remove 6
num=[2,4,6,8]
num[1]=10
print(num)

#given grade=[[80,85,90],[70,75,80],[60,65,70]] print the second student's score
grades=[[80,85,90],[70,75,80],[60,65,70]]
print(grades[1][1])


colors=['red','blue','green','red','yellow','purple']
colors.append('orange')
print(colors)
colors.insert(1,'black')
print(colors)
colors.remove('red')
print(colors)
colors.pop()
print(colors)
colors.reverse()
print(colors)
#colors.clear()

numbers=[1,20,4,50,34,]
numbers.sort() # reverse=true(sort in Desc Order should be inside sort
print(numbers)

#extending 1 list with another another
colors=['red','blue','green','red','yellow','purple']
numbers=[1,20,4,50,34,]
numbers.extend(colors)
print(numbers)
print(len(numbers))
print('maroon' in colors)