#User function Template for python3
class Solution:

    def findMaximum(self, arr):
        # code here
        arr.sort()
        return arr[len(arr)-1]
