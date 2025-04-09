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
#Insert a list of another student after bob list
students.insert(2,['Brian',"HTML","CSS","Swahili"])
print(students)