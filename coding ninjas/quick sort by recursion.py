def partition(a,si,ei):
    pivot=a[si]

    #find number of element smaller than pivot
    c=0
    for i in range(si, ei+1):
        if a[i] < pivot:
            c+=1

    a[si+c],a[si] = a[si], a[si+c]
    pivot_index= si+c
    i=si
    j=ei
    while i<j:
        if (a[i] < pivot):
            i=i+1
        elif a[j]>= pivot:
            j=j-1
        else:
            a[i],a[j]=a[j],a[i]
            i=i+1
            j=j-1
    return pivot_index
def quickSort(a,si,ei):
    if si>=ei:
        return
    pivot_index=partition(a, si, ei)
    quickSort(a,si, pivot_index - 1)
    quickSort(a,pivot_index + 1, ei)



a=[10,10,2,3,9,5,7,1,4]
x=quickSort(a,0,len(a)-1)
print(a)
