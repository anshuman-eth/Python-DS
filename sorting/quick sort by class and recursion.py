#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        if low>=high:
            return
        pivot_index=Solution.partition(self,arr,low,high)
        Solution.quickSort(self,arr,low,pivot_index-1)
        Solution.quickSort(self,arr,pivot_index+1,high)
    
    def partition(self,arr,low,high):
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

    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends