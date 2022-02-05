t=0
lst=[]
def palindrome(a):
    for i in a:
        while(True):
            b=str(i)
            c=b[::-1]
            if c==b:
                
                lst.append(b)

                break
            else:
                i+=1        
n=int(input("Enter the number of test cases:"))
a=list(map(int,input().strip().split()))[:n]
palindrome(a)
print(lst)