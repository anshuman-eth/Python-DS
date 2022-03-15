
class Solution:
    def isPalindrome(self, s):
        t=""
        for i in s:
            if i.isalnum():
                t=t+i
        x=t.lower()
        y=""
        for i in x:
            y=i+y
        if x==y:
            return True
        else:
            return False
if __name__ == "__main__":
    s=input()        
    l=Solution().isPalindrome(s)

    print(l)