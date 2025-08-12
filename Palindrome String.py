#User function Template for python3
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # code here
        if len(s)==1:
            return "true"
        else:
            return s==s[::-1]
