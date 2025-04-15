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
#terurn back to it and put input
def area_triangle(base,height):#the base and height inside the function are what we call parameters 
    area=base*height*0.5
    print(area)
area_triangle(20,50)
area_triangle(10,5)
x=int(input('enter base'))  
y=int(input('enter height '))

area_triangle(x,y)# this is when their is an 
                #input put the inputs in variables then when passing the arguments pass the variables as the arguments

#create a function area of a circle that the area use(3.14 for pi)
def area_circle(r, pi=3.14):#for default parameters once you add them hapo mwamzo you only put the radius and it comes always last
    area=pi*r*r #3.14*R*R
area_circle(40)   

2.# Prompt the user for a number either on a form input or the terminal. Depending on 
# whether the number is even or odd, display  either “odd” or “even” to the user.
# Hint: how does an even / odd number react differently when divided by 2?
def check_even_odd(number):
    if number % 2==0:
        print('even')
    else:
        print('odd')    
check_even_odd(100)       
num=int(input('enter number: '))# this is for when user has been told to input number 
check_even_odd(num)

5.# Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores them in three variables.
#  Return the largest of the three. Do this without using the the inbuilt max () function!
# The goal of this exercise is to think about some internals that programs normally take care of for us. 
#DONT PRINT INSIDE A FUNCTION STORE THEM IN VARIABLES E.G BELOW 
def largestof_thethree(person1,person2,person3):
    if person1>person2 and person1>person2:
         res=(person1,'is the largest number ') #can use a formated string print(f'[person 1}is the largest)
    elif person2>person1 and person2>person3: 
        res=(person2, 'is the largest number')  
    else:   
         res=(person3,'is the largest number')    
         return res
#store the function in a variable then print 
x=largestof_thethree(10,23,30)  
print(x)


    

    
   











