import sys
sys.setrecursionlimit(2000)
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
    


n=int(input())
x=fact(n)
print(x)