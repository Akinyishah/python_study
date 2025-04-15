# Write a program that prompts the user to input student marks. The input should be between 0 and 100.
# Then output the correct grade: A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40
# marks=list(range(0,101)) # HOW TO I CAP SOMETHING TO THE MENTIONED INPUT.
# print(marks)
# marks=int(input('enter your marks: '))
# if marks>79:
#     print('A')
# elif(marks<79) and marks>=60:
#     print('B-')   
# elif (marks<=59) and marks>49:
#     print('C')   
# elif (marks<=49) and marks>=40:
#     print('D-')
# else:
#     print('E')

marks=list(range(0,101)) #MUST HAVE NESTED IF BECAUSE WE ARE WORKING WITH SCORES FROM 0-100 ANYTHING 
                          #ABOUVE THAT IS INVALID MARKS 
marks=int(input('enter your marks: ')) 
if marks>=0 and marks<=100:
    if marks>79:
        res='A'
    elif marks<=79 and marks>=60:
        res='B'
    elif marks<=59 and marks>=49:
        res='C'
    elif marks<49 and marks>=40:
        res='D'
    else:
        res='E'
else:
    res='Invalid marks'

print(res)
    

                
        













