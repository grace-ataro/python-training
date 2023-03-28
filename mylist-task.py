#1
trainees=["John",[2,["James","Mary"]]]     
print("Original list",trainees)
print(trainees[1][0])
#2
print(trainees[1][1][0])
#3
trainees.append(56)
print(trainees)
#4
trainees=(trainees[1][1])
trainees.insert(1,"Mike")
print(trainees)
#5
trainees[1][0]=8
print(trainees)
#6
del trainees[0]
print(trainees)