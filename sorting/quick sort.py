def quickSort(a):
    si=0  #starting index
    ei=len(a)-1   #ending index
    c=0
    pivot=a[si]
    for i in range(si,ei+1):
        if a[i] < pivot:
            c=c+1
    a[si+c],a[si]=a[si],a[si+c]    
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] >a[j]:
                a[i],a[j]=a[j],a[i]
    print(c)
    print(a)
n=int(input())
a=list(map(int, input().strip().split()))[:n]
quickSort(a)