def quickSort(arr,low,high):
        # code here
        if low>=high:
            return
        pivot_index=partition(arr,low,high)
        quickSort(arr,low,pivot_index-1)
        quickSort(arr,pivot_index+1,high)
        
def partition(arr,low,high):
        # code here
        pivot=arr[low]
        c=0
        for i in range(low,high+1):
            if arr[i] <pivot:
                c+=1
        arr[low+c],arr[low]=arr[low],arr[low+c]
        pivot_index=low+c
        i=low
        j=high
        while i<j:
            if arr[i]<pivot:
                i+=1
            elif arr[j]>=pivot:
                j-=1
            else:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j-=1
        return pivot_index



arr=[10,10,2,3,9,5,7,1,4]
x=quickSort(arr,0,len(arr)-1)
print(arr)

