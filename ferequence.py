def k():
    list=["abc","xyz","aba","1221"]
    i=0
    a=[]
    while i<len(list):
        j=0
        b=[]
        count=0
        while j<len(list):
            if list[i] in list:
                if list[i]==list[j]:
                    count=count+1
                j=j+1
                b.append(list[i])
                b.append(count)
                if b not in a:
                    a.append(b)
                i=i+1
    print(a)
k()
