# Calculate the taxable income.
# i.e taxable_income = gross salary - (NSSF + NHDF + NHIF) 
def taxable_income():
    basic_salary=float(input('enter salary: '))
    benefits=float(input('enter benefits: '))
    gross_salary=basic_salary+benefits
    print(f'gross salary:{gross_salary:,.2f}')
    taxable_income=gross_salary-('nssf_contribution'+'nhdf_contribution'+'nhif_contribution')
taxable_income()    