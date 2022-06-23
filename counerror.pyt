def cha(a):
    i=0
    coun=0
    coun1=0
    while i<len(a):
        if a[i]>="A" and a[i]<="Z":
            coun=coun+1
        else: 
            coun1=coun1+1           
        i=i+1
    print("uper_case=",coun)
    print("lower_case=",coun1)
cha("The quick Brow Fox")

