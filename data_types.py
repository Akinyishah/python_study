#Introdusction to Stings
f_name='Shalyne'
print(type(f_name))

#Concanting Strings 
f_name='Shalyne'
s_name='Akinyi'
ful_name=f_name+' '+s_name
print(ful_name)

#Indexing and Slicing
text='my name is kevin'
print(text[13])
print(text[-3])
print(text[16:10:-3])

#given a string below extract the following using indexing and slicing
text1='python programming'
#extract python 
print(text1[0:5+1])
#extract programming
print(text1[7:17+1])
#extract the second character
print(text1[1])
#reverse the entire string -if you have not been told where to start from just put colon and then bring in -1
print(text1[::-1])

#string methods-inbuilt method used to manipulate strings

my_text='i  am  a  student'
print(my_text.upper()) # converts to uppercase
print(my_text.capitalize()) #makes the first letter Capital
print(my_text.casefold()) #makes the value of the variable not case sensitive
print(my_text.istitle())
print(my_text.format())
print(my_text.isnumeric())#is not numeric and anywhere their is an IS it will be boolean
print(my_text.split(' '))# splits to multiple parts
print(my_text.islower())
print(my_text.partition(' '))#partition the string into three parts using a given separator
print(my_text.replace('student','tutor'))
print(my_text.endswith('a'))
print(my_text.strip())
print(my_text.count('four'))
print(my_text.lower())
