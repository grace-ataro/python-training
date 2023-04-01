#Write a program that takes input of 2 values and adds them.
#The program should only accept numbers and floats only or otherwise display an error “invalid character entered” and take the user to re-enter the inputs .
num1=float(input("Enter num1:"))
num2=float(input("Enter num2:"))
if num1==float(num1) and num2==float(num2):
    num3=num1+num2
    print(num3)
else :
    print("Error,Invalid character entered")