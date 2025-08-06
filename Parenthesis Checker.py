class Solution:
    def isBalanced(self, s):
        # code here
        while '()' in s or '{}' in s or '[]' in s:
            s=s.replace('()','')
            s=s.replace('{}','')
            s=s.replace('[]','')
        return len(s)==0
