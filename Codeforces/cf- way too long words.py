def word(l):
    for i in l:
        if len(i)<=10:
            print(i)
        elif len(i)>10:
            print(i[0]+str(len(i)-2)+i[-1])

if __name__=="__main__":
    l=[]
    n=int(input())
    for i in range(n):
        m=str(input())
        l.append(m)
    word(l)
    print(l)

