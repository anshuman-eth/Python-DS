# def lastindex(arr,x):
#     l=len(arr)
#     if l==0:
#         return -1
#     smallArray=arr[1:]
#     newIndex=lastindex(smallArray, x)
#     if newIndex != -1:
#         return newIndex + 1
#     else:
#         if arr[0]==x:
#             return 0
#         else:
#             return -1

# arr=[1,2,3,4,2,3,3,4,5,3]
# x=int(input())
# p=lastindex(arr,x)
# print(p)



def lastindex(arr,x,si=0):
    l=len(arr)
    if si==l:
        return -1
    smallArray=lastindex(arr,x,si+1)
    if smallArray != -1:
        return smallArray
    else:
        if arr[si]==x:
            return si
        else:
            return -1


arr=[1,2,3,4,2,3,3,4,5,3]
x=int(input())
p=lastindex(arr,x)
print(p)