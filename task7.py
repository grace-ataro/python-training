#Write that prompts the user to input student marks.
#The input should be between 0 and 100.Then output the correct grade: 
#A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40
marks=float(input("Enter student marks:"))
if marks>=0 and marks<=100:
    if marks>79:
        print("A")
    if marks>=60 and marks<=79:
        print("B")
    if marks>=50 and marks<=59:
        print("C")
    if marks>=40 and marks<=49:
        print("D")
    if marks<40:
        print("E")
else:
    print("Invalid")
