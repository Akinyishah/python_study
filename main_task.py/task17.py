# Continue with the same program and calculate an individual’s NHDF using:
#  i.e NHDF = gross_salary *  0.015
def NHDF_contribution():
    basic_salary=float(input('enter salary: '))
    benefits=float(input('enter benefits: '))
    gross_salary=basic_salary+benefits
    print(f'gross salary:{gross_salary:,.2f}')
    nhdf=0.015 #15% of the gross salary 
    nhdf=gross_salary * 0.015
    print(f'nhdf: {nhdf:,.2f}')
NHDF_contribution()    