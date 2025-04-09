student1={
    "Name":"Alex",
    "Age":20,
    "Grade":90,
    "Subject":"Math"
}
#Accessing Values
# We must use the Key
#keys and values are separed by (:)
#the properties are separated by (,) property e.g"Name":"Alex","Age":20

print(student1["Subject"])

#adding values/updating values( when adding and updating MUST USE SQUARE BRACKETS)
#adding key
student1["Class"]="5W"
print(student1)

#updating keys(KEYS ARE CASE SENSITIVE)
student1["age"]=40
#adding profession
student1["Profession"]="Client Service"
print(student1)
#update Name
student1["Name"]="Shalyne"
print(student1)

#REMOVING ENRIES 
#pop()-remove specific element
student1.pop("Subject")
print(student1)
#clear()
#del-specifies what you wanna delete
#del student1["Subject"]

# NESTED DISCTIONARY
students={
    'tech004':{'name':'Amy','Gender':'Female','Marks':[85,70,60]},
    'tech005':{'name':'Levy','Gender':'Female','Marks':[90,80,60]},
    'tech009':{'name':'Sharon','Gender':'Female','Marks':[70,78,58]}
}
print(students['tech004']['Gender'])
print(students['tech005']['name'])
print(students['tech009']['Marks'][-1])
#dictionaryMethods
#.get method
student1={
    "Name":"Alex",
    "Age":20,
    "Grade":90,
    "Subject":"Math"
}
print(student1.get('Grade'))#returns a value of the specified key and NONE if the key does not exist.
print(student1.keys())#returns a list of the keys 
print(student1.values())# returns a list of all the values 
print(student1.items())# returns items(the property) on both in a tuple data type
student1.update({'Age':50,'marks':100,'Gender':'male'}) #adds or updates multiple entries at once
print(student1)
