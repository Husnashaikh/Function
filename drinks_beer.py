def drink():
    a=int(input("enter the age"))
    if a<=18:
        print("child will drink coffe/coke/tea")
    elif a<=21:
        print("young will drink beer")
    else:
        print("adult will drink whisky")
drink()