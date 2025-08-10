class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        s=set()
        l=[]
        for i in arr:
            if i not in s:
                s.add(i)
                l.append(i)
        l.sort()
        if len(l)<=1:
            return -1
        else:
            return l[len(l)-2]
