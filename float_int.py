#Convert a float to an integer with an inbuilt function in Python
#temp = 56.8926 to 57
temp=(56.8926)
temp=round(56.8926, )
print(temp)

#Convert the float below to give the results as follows
#temp = 56.8926 to 56.89 
temp=round(56.8926, 2)
print(temp)


#Convert the float below to give the results as follows
#temp = 56.8926 to 56.893 
temp=round(56.8926, 3)
print(temp)


#Convert the float below to give the results as follows
#temp=56.8926 to 8.926 
#NB: Use string  slice & concatenation, but have result as float 
temp=56.8926
temp_str=str(56.8926)
temp_str=temp_str[3:]
temp_str=temp_str[0]+ '.'+ temp_str[1:]
temp_str=float(temp_str)
print(temp_str)

#write a program that gets 2 inputs from the terminal then sum them
x=input('enter number : ')
y=input('enter number : ')
print(type(y))
x=int(x)
y=int(y)
sum=x+y
print(sum)

num=99
num1=5
result=num%num1
print(result)


num=100
num1=3
result=num//num1
print(result)

my_list = [[], [], []] #python interview basic question

def add_num(list, num):
     for sub_list in list:
        sub_list.append(num)
num = 1
add_num(my_list, num)
print(my_list)

num=1           #python interview basic question
my_list=[[],[],[]]
new_list=[]
for _ in my_list:
           new_list.append([num])
print(new_list)

num = 1         #python interview basic question
my_list = [[], [], []]
for sub in my_list:
    sub.append(num)
print(my_list)







