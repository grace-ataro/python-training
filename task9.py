#Write a program called stars.py.
#It should prompt the user for a number, and it should print the number of stars till the number entered.
num=int(input("Enter number: "))
symbol="*"
for i in range(1,num+1):
    print(symbol * i)