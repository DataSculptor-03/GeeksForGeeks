class Solution:
    def findSum(self,arr):
        # code here
        s=set()
        t=0
        a=[]
        for i in arr:
            if i not in s:
                s.add(i)
                a.append(i)
        for i in a:
            t+=i
        return t
