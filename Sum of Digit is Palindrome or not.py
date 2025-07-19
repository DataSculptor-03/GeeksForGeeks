class Solution:
    def isDigitSumPalindrome(self, n):
        #code here
        if(1<=n<=10**9):
            s=0
            while(n>0):
                rem=n%10
                s+=rem
                n=n//10
        if(pallindrome(s)):
            return 1
        else:
            return 0
def pallindrome(n):
    rev=str(n)[::-1]
    if(n==int(rev)):
        return 1
    else:
        return 0
