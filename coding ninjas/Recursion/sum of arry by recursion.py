def sum(arr):
    t=0
    l=len(arr)
    if l==1:
        return arr[0]
    if l>1:
        newlist=arr[1:]
        t=sum(newlist)+arr[0]
        return t



n=int(input())
arr=list(map(int, input().strip().split()))[:n]
x=sum(arr)
print(x)