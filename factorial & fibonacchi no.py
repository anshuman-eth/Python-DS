def fun1(n):
    j=1
    for i in range(n):
        j=j*(i+1)
    return j

def fun2(m):
    if m==1:
        return 1
    else:
        return m*fun2(m-1)

def fun3(n):
    if n==1:
        return 0
    if n==2:
        return 1
    else:
        return fun3(n-1) + fun3(n-2)



n=int(input("Enter a number to calculate factorial:"))
x=fun1(n)
print(x)
y=fun2(n)
print(y)
z=fun3(n)
print(z)