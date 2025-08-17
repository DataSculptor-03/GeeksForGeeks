class Solution:
    def countZeroes(self, arr):
        # code here
        count=0
        for i in range(len(arr)):
            if(arr[i]==0):
                count+=1
        return count
