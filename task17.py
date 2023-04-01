#To calculate the Employees Payee, you need to find the gross salary first then find the taxable income (this is the gross salary less the NHIF value) 
#i.e taxable_income = gross salary - NSSF
#Continue with the same program and find the person's PAYEE .
salary=float(input("Enter your basic salary: "))
benefits=float(input("Enter your benefits: "))
gross=salary+benefits
if (gross>=6000 and gross<=18000):
    nssf=0.06*gross
    print(nssf)
else:
    nssf=1080
    print(nssf*2)
taxableincome=(str(gross-nssf))
income=(float(gross-nssf))
print("taxable income is:" + taxableincome)
if (income<=24000):
    payee= 0
    print(payee)
elif(income>24000 and income<=32333):
    payee=((0.1*24000)+(income-24000)*0.25)-2400
    print(payee)
elif(income>32333):
    payee=((0.1*24000)+(income-32333)*0.3+(8333*0.25))-2400
    print(payee)
else:
    print("Invalid amount entered"input("Enter amount from 0: "))
