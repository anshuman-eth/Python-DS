def palindrome(s):
    l=len(s)
    if l<2:
        return True
    if s[0] == s[l-1]:
        return palindrome(s[1:l-1])
    else:
        return False

s=input()
x=palindrome(s)
print(x)