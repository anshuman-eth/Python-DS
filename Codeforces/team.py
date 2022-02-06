def team(a,n):
    t=0
    p=0
    z=0
    while(z!=n):
        for j in a:
            if j.isnumeric()==True:
                t=t+int(j)
        if t>1:
            p+=1
        z=z+1
    print(p)

            

if __name__=="__main__":
    l=[]
    n=int(input())
    for i in range(n):
        m=str(input())
        l.append(m)
    for a in l:
        team(a,n)

    