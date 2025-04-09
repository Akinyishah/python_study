#trainees ["John",[2,["James,"Mary"]]]
trainees=["John",[2,["James","Mary"]]]

#Display 2 from the list
print(trainees[1][0])

#Output James from the list
print(trainees[1][1][0]) 

#using a method add 56 at the end of the list
trainees=["John",[2,["James","Mary"]]]
trainees.append(56)
print(trainees)

#using a method add the name Mike between James and Mary
print(trainees[1][1])
trainees[1][1].insert(1,"Mike")
print(trainees)

#change the value of 2 to 8
trainees[1][0]=8
print(trainees)

#remove John and Mary from the list
trainees.remove('John',)
print(trainees)
trainees=[[8, ['James', 'Mike', 'Mary']], 56]
print(trainees[0][1])
trainees[0][1].remove('Mary')
print(trainees)

#using a function, determine the length of the list 
print(len(trainees))

students=[["Alice",["Math","Physics","English"]],
["Bob",["Biology","Chemistry","History"]],
["Charlie",["Computer Science","Math","Art"]]]

#Display English
print(students[0][1][2])
#Change Charlie to Alex
students[2][0]='Alex'
print(students)
#Remove Math
students[0][1].pop(0)
print(students)
students[2][1].remove('Math')
print(students)

#Insert Java before Art
students[2][1].insert(1,"java")
print(students)
#Insert a list of anotherb student after bob list
students.insert(2,['Brian',"HTML","CSS","Swahili"])
print(students)
