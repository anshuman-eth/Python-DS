#Normal sortibg technique
# def sort(arr,n):
#     for i in range(0, n):
#         for j in range(i+1,n):
#             print(arr[i],arr[j])
#             if arr[i]<arr[j]:
#                 arr[i],arr[j]=arr[j],arr[i]
#     return arr
        
# n=int(input())
# arr=list(map(int,input().strip().split()))[:n]
# x=sort(arr,n)
# print(x)

def merge(a1,a2,arr):
    i=0
    j=0
    k=0
    while i < len(a1) and j < len(a2):
        if (a1[i] < a2[j]):
            arr[k]=a1[i]
            k=k+1
            i=i+1
        else:
            arr[k]=a2[j]
            k=k+1
            j=j+1

    while i < len(a1):
        arr[k]=a1[i]
        k=k+1
        i=i+1
    while j <len(a2):
        arr[k]=a2[j]
        k=k+1
        j=j+1

def merge_sort(arr):
    if len(arr)==0 or len(arr)==1:
        return 
    mid=len(arr)//2
    a1=arr[0:mid]
    a2=arr[mid:]
    merge_sort(a1)
    merge_sort(a2)
    merge(a1,a2,arr)

n=int(input())
arr=list(map(int,input().strip().split()))[:n]
merge_sort(arr)
print(arr)