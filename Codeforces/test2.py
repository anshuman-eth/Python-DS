def team(l):
    c=0
    for i in l:
        if i.count("1")>=2:
            c+=1

    print(c)

         
    
            
if __name__=="__main__":
    l=[]
    n=int(input())
    for i in range(n):
        m=str(input())
        l.append(m)
    team(l)