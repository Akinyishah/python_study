def hello(): #when creating functions must start with def which is the key word then the function_name,
             #when you want it appear on the terminal you must call/invoke the function name
    print('hello TechCamp')
hello()       #this calling/invoking the fuction so that it can run and appear on the terminal. YOU MUST CALL IT FOR IT TO RUN
              #when creating a block of code use the: and ensure that indentation is there

#create a function called welcome_message()that prints'welcome python'
def welcome_message():
    print('Welcome Python')
welcome_message()   

#USING THE FUNCTION -DEF
1.#Write a program that prompts the user to enter the base and height of a triangle and returns its area.
def area_triangle(base,height):#the base and height inside the function are what we call parameters 
    area=base*height*0.5
    print(area)
x=int(input('enter base '))  
y=int(input('enter height '))
area_triangle(x,y)

2.#create a function area of a circle that the area use(3.14 for pi)
#for default parameters once you add them hapo mwanzo you only put the radius and it comes always last
#3.14*R*R
def area_circle(r, pi=3.14):
    area=pi*r*r 
    print(area) 
z=int(input('enter radius: '))    
area_circle(z,3.14)   

2.# Prompt the user for a number either on a form input or the terminal. Depending on 
# whether the number is even or odd, display  either “odd” or “even” to the user.
# Hint: how does an even / odd number react differently when divided by 2?
def check_even_odd(number):
    if number % 2==0:
        print('even')
    else:
        print('odd')    
#check_even_odd(100)
#this is for when user has been told to input number       
num=int(input('enter number: '))
check_even_odd(num)

5.#Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores them in three variables.
# Return the largest of the three. Do this without using the the inbuilt max () function!
#The goal of this exercise is to think about some internals that programs normally take care of for us. 
#DONT PRINT INSIDE A FUNCTION STORE THEM IN VARIABLES E.G BELOW  
def largestof_thethree(User1,User2,User3):
    notes='is the largest'
    if User1>User2 and User1>User3:
         return f"User1 {notes}"       #can use a formated string print(f'[person 1}is the largest)
    elif User2>User1 and User2>User3: 
         return f"User2 {notes}"
    else:   
         return f"User3 {notes}"         
p1=int(input('enter num1: '))
p2=int(input('enter num2: '))
p3=int(input('enter num3: '))

#for such ensure to create a variable.
x=largestof_thethree(p1,p2,p3)      
print(x)


    
   











