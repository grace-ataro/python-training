#Prompt the user for a number either on a form input or the terminal. 
#Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
#Extras:
#If the number is a multiple of 4, display out a different message.
num=input("Enter a number: ")
num_int=float(num)
if num_int % 4==0:
   print("The Number Is a Multiple of 4")
elif num_int % 2==0:
    print("Even")
else:
    print("Odd")
