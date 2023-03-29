mynum = float(input("Enter marks to test"))
if (mynum>=0) and (mynum<=100):
 if mynum >=70:
    print("High")
 elif mynum < 70 and mynum >40:
    print("Medium")
 else:print("Low")
else:
  print("Number invalid")
