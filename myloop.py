ls1=range(1,20)
ls2=list(ls1)
print(ls1)
for i in ls1:
    print("i is",i)
mydata=["Nrb","Msa","Ksm","Eld","Nkr"]
mydataindexes=list(range(0,len(mydata)))
print(mydataindexes)
for i in[0,1,2,3,4]:
    if mydata[i]=="Ksm":
       mydata[i]="Kisumu"
       break
    else:
        pass
print(mydata)