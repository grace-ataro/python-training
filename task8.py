#Write a program that takes as input the speed of a car e.g 80. 
#If the speed is less than 70, it should print “Ok”. 
#Otherwise, for every 5 km/s above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points.
#For example, if the speed is 80, it should print: “Points: 2”. If the driver gets more than 12 points, the function should print: “License suspended”.
speed=float(input("Enter speed of car:"))
if speed<70:
    print("Ok")
else:
    demerits=str((speed-70)/5)
    print("Points:",demerits)
    if float(demerits)>12:
        print("License suspended")
