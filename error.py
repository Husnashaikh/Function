def prime():
    a=int(input("enter the number"))
    i=0
    while i<=a:
        if a%1==0 and a%2!=0:
            print(i,"prime no")
        else:
            print(i,"not prime no")
        i=i+1
prime()
