# def calc_nhif(gross):
#     gross='benefits'+'salary'
#     benefits=int(input('enter number: '))
#     salary=int(input('enter number: '))
#     return gross
#     notes='is my nhif contribution'
#     if gross>9000:
#         return f'150 {notes}'
#     if:
#         return f'300 {notes}'
    
# salary=input('enter your salsry: ')

# NHIF=calc_nhif(gross)


def cal_payee(taxable_income):
    notes='is your PAYE'
    if taxable_income>=0 and taxable_income<=24000:
        payee=0
        return payee
    elif taxable_income>24000 and taxable_income<=32333:
        payee=(24000*0.1)+((taxable_income-24000)*0.25)-2400
        return  f'{payee}{notes}'
    elif taxable_income>32333 and taxable_income<=500000:
        payee=(24000*0.1)+(8333*0.25)+((taxable_income-32333)*0.3)-2400
        return  f'{payee}{notes}'
    elif taxable_income>500000 and taxable_income<=800000:
        payee=(24000*0.1)+(8333*0.25)+(467667*0.3)+((taxable_income-500000)*0.325)-2400
        return  f'{payee}{notes}'
    else:
        payee=(24000*0.1)+(8333*0.25)+(467667*0.3)+(300000*0.325)+((taxable_income-800000)*0.35)-2400
        return  f'{payee}{notes}'
payee=cal_payee(taxable_income)
print(payee)