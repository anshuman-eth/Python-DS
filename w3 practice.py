def divisor(n,mn,mx):
    if mn!=mx:
        for i in range(mn,mx+1):
            if n%i==0:
                print(f"{i} is a divisor of {n}.")
            else: 
                print(f"{i} is not a divisor of {n}.")







    else:
        if n%mx==0:
            print(f"{mx} is a divisor of {n}.") 
        else:
            print(f"{mx} is not a divisor of {n}.") 







n=int(input("Input the number of apples Harry Potter has got:"))
mn=int(input("Enter the minimum range:"))
mx=int(input("Enter the maximum range:"))
x=divisor(n,mn,mx)