arr=[5,45,23,4]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]<arr[j]:
            arr[i],arr[j]=arr[j],arr[i]

print(arr)