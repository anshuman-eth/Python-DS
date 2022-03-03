def isPalindrome(x):
        x=str(x)
        y=str(x)
        for i in range(len(y)//2):
            y[i],y[len(y-i-1)]=y[len(y-i-1)],y[i]
        if y==x:
            return 'true'
        else:
            return 'false'


x=121
p=isPalindrome(x)
print(p)