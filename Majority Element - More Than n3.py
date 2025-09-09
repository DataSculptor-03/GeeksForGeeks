class Solution:
    def findMajority(self, arr):
        # code here
        s=set()
        li=[]
        l=[]
        length=len(arr)
        for i in arr:
            if i not in s:
                s.add(i)
                l.append(i)
        l.sort()
        for i in l:
            c=arr.count(i)
            if(c>length//3):
                li.append(i)
        return li
