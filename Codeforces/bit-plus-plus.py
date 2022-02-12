
def bit(m):
    print(m)
    t=0
    for i in m:
        if i=="X++" or i=="++X":
            t=t+1
        elif i=="--X" or i=="X--":
            t=t-1
    return abs(t)







if __name__=="__main__":
    n=int(input())
    m=[]
    for i in range(n):
        m.append(input())
    x=bit(m)
    print(x)