n=int(input("Enter an interger to print the pattern"))
b=int(input("Enter '1' to print in symmatric order or enter '0' to print in assemetric direction."))
l="*"
m=n*l
if bool(b)==True:
    for i in range(n):
        print(l)
        l=l+"*"
elif bool(b)==False:
    for i in range(n,0,-1):
        print(m)
        m=m[:-1]
else:
    print("Wrong input")      