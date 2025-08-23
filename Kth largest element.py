#User function Template for python3
class Solution:
    #Function to return kth largest element from an array.
    def kthLargest(self,arr,k):
        
        # code here
        arr.sort()
        return arr[-k]
