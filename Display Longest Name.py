class Solution:
    def longest(self, arr):
        # code here
        big = arr[0]
        for i in range(1, len(arr)):
            if len(big) < len(arr[i]):
                big = arr[i]
        return big         
