#User function Template for python3
class Solution:
    def findKRotation(self, arr):
        min_val = arr[0]
        min_index = 0
        for i in range(1, len(arr)):
            if arr[i] < min_val:
                min_val = arr[i]
                min_index = i
        return min_index
