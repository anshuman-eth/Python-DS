def sum(n):
    if n==0:
        return 1
    l=round(1/(2**n)+sum (n-1),5)
    return l
    
n=int(input())
x=sum(n)
print(x)