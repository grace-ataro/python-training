#Continue with the program above(task15), then use  the gross salary to find the NSSF.
salary=float(input("Enter your basic salary: "))
benefits=float(input("Enter your benefits: "))
gross=salary+benefits
if (gross>=6000 and gross<=18000):
    nssf=0.06*gross
    print(nssf)
else:
    nssf=1080
    print(nssf*2)
