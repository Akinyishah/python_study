1.#Write a program that prompts the user to enter the base and height of a triangle and returns its area.
#terurn back to it and put input
# base=50
# height=100
# area=(1/2)*base*height
# print(area)

# def area_triangle():
#     base=int(input)

# area_triangle(20,50)
# area_triangle(10,5)


def area_triangle(base,height):#the base and height inside the function are what we call parameters 
    area=base*height*0.5
    print(area)
x=int(input('enter base '))  
y=int(input('enter height '))
area_triangle(x,y)

