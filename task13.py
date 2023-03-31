#Write a program that takes the email and password as input from a user
#and checks if they are equal to “admin@mail.com” and password is “Admin@123” ,
#if so then print  “Login is Successful” and if not print “Invalid username or password”. 
#ONLY accept 3 tries after which it notifies you that you have been blocked.
email=input("Enter your Email: ")
password=input("Enter your Password: ")
attempts=3
for i in range(1,attempts):
    if (email=="admin@mail.com" and password=="Admin@123"):
        print("Login is Successful")
    else:
        print("Invalid username and password")

if attempts>3:
    print("You have been blocked")