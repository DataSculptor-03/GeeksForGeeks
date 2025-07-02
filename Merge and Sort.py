#User function Template for python3
class Solution:
    def mergeNsort(self, arr, brr):
        # Write your code here
        c=arr+brr
        c.sort()
        d=[]
        e=set()
        for i in c:
            if i not in e:
                e.add(i)
                d.append(i)
        return d
