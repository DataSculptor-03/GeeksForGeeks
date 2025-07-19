class Solution:
    def customSort(self, arr):
        # code here
        a=[]
        b=[]
        l=len(arr)
        for i in range(0,l//2):
            a.append(arr[i])
        for i in range(l//2,l):
            b.append(arr[i])
        a.sort()
        b.sort(reverse=True)
        c=a+b
        return c
        
