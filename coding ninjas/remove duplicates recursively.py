def removeD(s):
    t=""
    for i in s:
        if i not in t:
            t=t+i
    print(t)




s=input()
x=removeD(s)
print(x)
