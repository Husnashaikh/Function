def eve():
    i=0
    b=[]
    while i<10:
        num=int(input("enter the number"))
        b.append(num)
        i=i+1
        print(b)
    i=0
    while i<len(b):
        if i%2==0:
            print(i,"=even number",i*100)
        else:
            print(i,"=odd number",i*-1)
        i=i+1
eve()

























# f it is even, then multiply it by 100
# If it is odd, then multiply it by -1 
# Sample Input:
#     23
#     42 
#     41 
#     1
# Sample Output:
#     -23 
#     4200 
#     -41 
#     -1
