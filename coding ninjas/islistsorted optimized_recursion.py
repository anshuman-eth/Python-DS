def isSortedbetter(a,si):
    l=len(a)
    if si==l-1 or si==l:
        return True
    if a[si]>a[si+1]:
        return False
    isSmallpartsorted=isSortedbetter(a,si+1)
    return isSmallpartsorted

a=[1,2,2,3,4,5]
si=int(input())
x=isSortedbetter(a,si)
print(x)