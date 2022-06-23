def remove(a):
    i=0
    b=[]
    while i<len(a):
        d=str(a[i])
        c=""
        j=0
        while j<len(d):
            if d[j]!="0":
                c=c+d[j]
            j=j+1
        b.append(int(c))
        i=i+1
    print(b)
remove([1450,960000,1050,-1050])
