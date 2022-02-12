import random

def rohan(l,n):
    a=random.randint((n*3)+1,n*4+(n-1))
    l[3]=a
    print(F"Rohan's table is {l}")
    for i in range(len(l)):
        t=n*(i+1)
        if l[i]==n*(i+1):
            pass
        else:
            print(f"correct answer is {n}*{i+1}={t}")

if __name__=="__main__":
    n=int(input("Enter an integer to print it's table:"))
    l=[]
    for i in range(1,11):
        i=n*i
        l.append(i)
    rohan(l,n)