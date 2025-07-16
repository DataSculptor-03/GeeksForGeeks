class Solution:
    def find_unique(self, k, arr):
        #code here
        x=[0]*(2*(10**5))
        for i in arr:
            x[i]+=1
        for i in arr:
            if(x[i]==1):
                return i
