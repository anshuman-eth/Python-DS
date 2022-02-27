# def isSorted(list):
#     l=len(list)
#     if l==0 or l==1:
#         return True
#     if list[0]>list[1]:
#         return False
#     smalllist=list[1:]
#     isListsorted=isSorted(smalllist)
#     if isListsorted:
#         return True
#     else:return False


# list=[0]
# a=isSorted(list)
# print(a)
def isSorted(list,si=0):
    l=len(list)
    if si==l-1 or si==l:
        return True
    if list[si]>list[si+1]:
        return False
    isListsorted=isSorted(list,si+1)
    return isListsorted

list=[1,0]
a=isSorted(list)
print(a)