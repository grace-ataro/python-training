#Implement a program that takes 3 form inputs or from the terminal, and stores them in three variables.
#Return the largest of the three. Do this without using the the inbuilt max () function!
num1=float(input("Enter num1"))
num2=float(input("Enter num2"))
num3=float(input("Enter num3"))

if(num1>num2) and (num1>num3):
    print(num1)
elif(num2>num1) and (num2>num3):
    print(num2)
elif(num3>num1) and (num3>num2):
    print(num3)
else:
    print("They are Equal")
