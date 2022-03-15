from tkinter import E


def binarySearch(a,x,si,li):
    if si > li:
        return -1
    mid=(li+si)//2
    if a[mid]==x:
        return mid
    elif a[mid] > x:
        return binarySearch(a,x,si,mid - 1)
    else:
        return binarySearch(a,x, mid + 1 ,li)


a=[1,2,4,5,6,7,8,9,22,45,66,88,99]
x=88
si=0
li=len(a)-1
p=binarySearch(a,x,si,li)
print(p)