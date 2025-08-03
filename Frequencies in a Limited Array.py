class Solution:
    def frequencyCount(self, arr):
        #  code here
        x=[0]*len(arr)
        for i in arr:
            x[i-1]+=1
        return x
