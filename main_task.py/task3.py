# Write a program which gets a phone number from a form input or terminal. 
# Validates the phone number by checking if it starts with +254.. or 07.. or 7… or 254.. or 01... or  1.. 
# Convert the number to start with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”
cell_number=input('your cell number: ')
if cell_number[0:4]=='+254' and len(cell_number)==13:
    valid =f'{cell_number} is a valid  cell_number'   
elif cell_number[0:2]=='07' and len(cell_number)==10:
    valid =f'{cell_number} is a valid  cell_number'
    cell_number='+254' +cell_number[1:]
    valid =f'{cell_number} is a valid  cell_number'
elif cell_number[0]== '7' and len(cell_number)==9:
     cell_number='+254' +cell_number
     valid =f'{cell_number} is a valid  cell_number' 
elif cell_number[0:3]=='254' and len(cell_number)==12:
     cell_number='+' +cell_number
     valid =f'{cell_number} is a valid  cell_number' 
elif cell_number[0:2]=='01' and len(cell_number)==10:
     cell_number='+254'+cell_number
     valid =f'{cell_number} is a valid  cell_number' 
elif cell_number[0]== '1' and len(cell_number)==9:
     cell_number='+254' +cell_number
     valid =f'{cell_number} is a valid  cell_number'
else:
    valid=('invalid cell_number')           
print(valid)






    
    




# elif cell_number[0:2]=='07' and len(cell_number)==10:
#     cell_number='+254' +cell_number[1:]
#     valid =f'{cell_number} is a valid  cell_number'    
# elif cell_number[0]=='7' and len(cell_number)==9:
#     cell_number='+254' +cell_number  
#     valid =f'{cell_number} is a valid  cell_number'
# elif cell_number[0:3]== '254' and len(cell_number)==13:
#     cell_number='+254'+cell_number 
#     valid =f'{cell_number} is a valid  cell_number'

# print(valid)             
# def validate_phone(cell_number):       #then bring in the if statement and ensure indentation CHECK PICS