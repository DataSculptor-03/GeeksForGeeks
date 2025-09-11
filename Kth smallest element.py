class Solution:
    def kthSmallest(self, arr, k):
        #code here 
        arr.sort()
        return arr[k-1]
