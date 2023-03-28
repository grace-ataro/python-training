#TASK
#CREATE A FILE CALLED mylargest.py TAKE INPUT FROM USER 3 NUMBERS 
# SEPARATELY. PRINTN THE LARGEST OF THE 3. IF ALL ARE EQUAL, PRINT EQUAL.
num1=float(input("Enter num1"))
num2=float(input("Enter num2"))
num3=float(input("Enter num3"))

if(num1>num2) and (num1>num3):
    print(num1)
if(num2>num1) and (num2>num3):
    print(num2)
if(num3>num1) and (num3>num2):
    print(num3)
