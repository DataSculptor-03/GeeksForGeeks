class Solution:
    def findElements(self,arr):
        # Your code goes here
        arr.sort()
        return arr[0:len(arr)-2]
