class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=len(s)
        if l<2:
            return True
        elif s[0]==s[l-1]:
            return Solution.validPalindrome(self, s[1:l-1])
        else:
            return False

if __name__=='__main__':
    s=input()
    x=Solution().validPalindrome(s)
    print(x)