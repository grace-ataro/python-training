#Write a program which gets a phone number from a form input or terminal. 
#Validates the phone number by checking if it starts with +254.. or 07.. or 71… or 254.. or 01...
# Convert the number to start with +254… 
#e.g if a user enters “0712345678”, the program should display “+254712345678”
#e.g if a user enters “0112345678”, the program should display “+254112345678”
#e.g if a user enters “712345678”, the program should display “+254712345678”
phonenumber=input("Enter Phone Number: ")
phonenumber_int=float(phonenumber)
print("+254", not "254" or "07" or "71" or "01")