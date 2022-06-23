def num():
    a=int(input("enter the umber"))
    b=int(input("enter the number"))
    if a%2==0 and b%2==0:
        print("both are even number",a,b)
    else:
        print("both are not even number",a,b)
num()

# QUESTION:2
def num(a,b):
    i=0
    while i<len(a):
        if a[i]%2==0 and b[i]%2==0:
            print("both are even no")
        else:
            print("both are not even no")
        i=i+1
num([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87])
