def power(n,m):
    t=1
    for i in range(1,m+1):
        t=t*n
    return t


n,m=map(int,input().strip().split())

x=power(n,m)
print(x)