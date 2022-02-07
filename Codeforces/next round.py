
def next_round(a,y):
    t=0
    for i in a:
        if i>=a[y-1] and i>0:
            t+=1
    print(t)
        
x, y = map(int, input().split())
a=list(map(int,input().strip().split()))[:x]
next_round(a,y)