def sum(a,b,c):
    i=0
    sum=0
    coun=0
    while i<a:
        sum=a+b+c
        i=i+1
        coun=coun+1
        print(sum)
        aver=sum/coun
        print(aver)
a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the numbdr"))
sum(a,b,c)