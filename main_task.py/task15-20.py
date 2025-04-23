# Write a program that takes input of someone's basic salary and benefits, adds them to find the gross salary then uses 
# the gross salary to find the NHIF. 
# To find the Kenya NHIF Rate using THIS LINK:
def calc_gross_salary(basic,benefits):
    gross =basic+benefits
    return gross
basic_salary=float(input('enter basic salary: '))
benefits=float(input('enter benefits: '))
gross_salary=calc_gross_salary(basic_salary,benefits)
print(gross_salary)
 
#calculating NHIF
def calc_nhif(gross):
    if gross<=5999:
        nhif_contribution=150
    elif gross>=6000 and gross<=7999:
        nhif_contribution=300
    elif gross>=8000 and gross<=11999:
        nhif_contribution=400
    elif gross>=12000 and gross<=14999:
        nhif_contribution=500
    elif gross>=15000 and gross<=19999:
        nhif_contribution=600
    elif gross>=20000 and gross<=24999:
        nhif_contribution=750
    elif gross>=25000 and gross<=29999:
        nhif_contribution=850
    elif gross>=30000 and gross<=34999:
        nhif_contribution=900
    elif gross>=35000 and gross<=39999:
        nhif_contribution=950
    elif gross>40000 and gross<=44999:
        nhif_contribution=1000
    elif gross>=45000 and gross<49999:
        nhif_contribution=1100
    elif gross>=50000 and gross<59999:
        nhif_contribution=1200
    elif gross>=60000 and gross<69999:
        nhif_contribution=1300
    elif gross>=70000 and gross<=79999:
        nhif_contribution=1400 
    elif gross>=80000 and gross<=89999:
        nhif_contribution=1500
    elif gross>=90000 and gross<=99999:
        nhif_contribution=1600
    else:
        nhif_contribution=1700 
    return nhif_contribution
NHIF=calc_nhif(gross_salary)  
print(NHIF)

#calculate NSSF-NUMBER16

def calc_nssf(gross,nssf_rate=0.06):
    if gross<=18000:
        # nssf_rate=0.06
        nssf=gross*nssf_rate
    else:
        nssf=18000*nssf_rate
    return nssf
NSSF=calc_nssf(gross_salary)       
print(NSSF)

#calculate NHDF-NUMBER 17
def calc_nhdf(gross,nhdf_rate=0.015):
    nhdf=gross*nhdf_rate
    return nhdf
NHDF=calc_nhdf(gross_salary)
print(NHDF)



# Calculate the taxable income.
# i.e taxable_income = gross salary - (NSSF + NHDF + NHIF) 
def calc_taxableincome(gross,NSSF,NHDF,NHIF):
    taxable_income=gross_salary - (NSSF + NHDF + NHIF) 
    return taxable_income
taxable_income=calc_taxableincome(gross_salary,NSSF,NHDF,NHIF )
print(taxable_income)

# Continue with the same program and find the person's PAYEE using the taxable income above.
# Find the Kenya PAYEE Tax Rate using THIS LINK
def cal_payee(taxable_income):
    if taxable_income>=0 and taxable_income<=24000:
        payee=0
        return payee
    elif taxable_income>32333 and taxable_income<=500000:
        payee=(24000*0.1)+(8333*0.25)+((taxable_income-32333)*0.3)-2400
        return payee
    elif taxable_income>500000 and taxable_income<=800000:
        payee=(24000*0.1)+(8333*0.25)+(467667*0.3)+((taxable_income-500000)*0.325)-2400
        return payee
    else:
        payee=(24000*0.1)+(8333*0.25)+(467667*0.3)+(300000*0.325)+((taxable_income-800000)*0.35)-2400
        return payee
payee=cal_payee(taxable_income)
print(payee)


# Continue with the same program and calculate an individual’s Net Salary using:
#  net_salary = gross_salary - (nhif + nhdf +  nssf + payee)
def calc_netsalary(gross,NHIF, NHDF, NSSF, payee):
    net_salary=gross_salary - (NHIF + NHDF +  NSSF + payee)
    return net_salary                                        #return is used to send results back to the caller
net_salary=calc_netsalary(gross_salary,NHIF, NHDF, NSSF, payee)
print(net_salary)      
   


