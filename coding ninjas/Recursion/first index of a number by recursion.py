

# def index(a,x):
#     l=len(a)
#     if l==0:
#         return -1
#     if a[0]==x:
#         return 0
#     smallArray=a[1:]
#     smallListoutput=index(smallArray,x)
#     if smallListoutput == -1:
#         return -1
#     else:
#         return smallListoutput + 1
    
# n=int(input())
# a=list(map(int,input().strip().split()))[:n]
# x=int(input())
# p=index(a,x)
# print(p)


def index(a,x,si=0):
    l=len(a)
    if si==l:
        return -1
    if a[si]==x:
        return si

    smallListoutput=index(a,x,si+1)
    return smallListoutput


n=int(input())
a=list(map(int,input().strip().split()))[:n]
x=int(input())
p=index(a,x)
print(p)