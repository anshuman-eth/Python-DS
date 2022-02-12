def simpleArraySum(ar):
    t=0
    s=0
    a=ar[0]
    b=ar[0]
    # b=
    for i in ar:
        if i>a:
            a=i
            t=t+1
        elif i<b:
            b=i
            s=s+1
    print(t,s)

        
    # Write your code here

if __name__ == '__main__':
    x=int(input())
    a=list(map(int,input().strip().split()))[:x]
    simpleArraySum(a)