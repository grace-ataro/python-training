#Write a program that takes input of someone's basic salary and benefits,
#adds them to find the gross salary then uses  the gross salary to find the NHIF. 
salary=float(input("Enter your basic salary: "))
benefits=float(input("Enter your benefits: "))
gross=salary+benefits
if (gross>=5999):
    nhif=150
    print(nhif)
elif(gross>=6000 and gross <=7999):
    nhif=300
    print(nhif)
elif(gross>=8000 and gross<=11999):
    nhif=400
    print(nhif)
elif(gross>=12000 and gross<=14999):
    nhif=500
    print(nhif)
elif(gross>=15000 and gross<=19999):
    nhif=600
    print(nhif)
elif(gross>=20000 and gross<=24999):
    nhif=750
    print(nhif)
elif(gross>=25000 and gross<=29999):
    nhif=850
    print(nhif)
elif(gross>=30000 and gross<=34999):
    nhif=900
    print(nhif)
elif(gross>=35000 and gross<=39999):
    nhif=950
    print(nhif)
elif(gross>=40000 and gross<=44999):
    nhif=1000
    print(nhif)
elif(gross>=45000 and gross<=49999):
    nhif=1100
    print(nhif)
elif(gross>=50000 and gross<=59999):
    nhif=1200
    print(nhif)
elif(gross>=60000 and gross<=69999):
    nhif=1300
    print(nhif)
elif(gross>=70000 and gross<=79999):
    nhif=1400
    print(nhif)
elif(gross>=80000 and gross<=89999):
    nhif=1500
    print(nhif)
elif(gross>=90000 and gross<=99999):
    nhif=1600
    print(nhif)
elif(gross>=100000):
    nhif=1700
    print(nhif)
else:
    print("Enter amount wihin range")