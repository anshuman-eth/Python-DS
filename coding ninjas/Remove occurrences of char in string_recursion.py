def remove(s,x):
    if len(s)==0:
        return ""
    smallOutput=remove(s[1:],x)
    if s[0]==x:
        return smallOutput
    else:
        return s[0] + smallOutput

s=input()
x=input()
p=remove(s,x)
print(p)