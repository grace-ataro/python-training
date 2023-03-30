#Write a program which gets a phone number from a form input or terminal. 
#Validates the phone number by checking if it starts with +254.. or 07.. or 71… or 254.. or 01...
# Convert the number to start with +254… 
#e.g if a user enters “0712345678”, the program should display “+254712345678”
#e.g if a user enters “0112345678”, the program should display “+254112345678”
#e.g if a user enters “712345678”, the program should display “+254712345678”
num=input("Enter your phone number: ")
if (num[0]=="0" and num[1]=="7"):
    num="+254" + num[1:]
    print(num)
elif (num[0]=="0" and num[1]=="1"):
    num="+254" + num[1:]
    print(num)
elif (num[0]=="7"):
    num="+254" + num
    print(num)
elif (num[0]=="2" and num[1]=="5" and num[2]=="4"):
    num="+" + num
    print(num)
else:
    print("false")
   