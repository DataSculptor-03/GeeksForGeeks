#User function template for Python 3

class Solution:
    def majorityElement(self, arr):
        #code here
        x=[0]*10**5
        for i in arr:
            x[i]+=1
        for i in arr:
            if(x[i]>(len(arr)//2)):
                return i
        return -1
