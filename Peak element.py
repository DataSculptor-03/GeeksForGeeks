
class Solution:   
    def peakElement(self,arr):
        # Code here
        n = len(arr)

        # Handle edge cases for single element
        if n == 1:
            return 0

        # Check if the first element is a peak
        if arr[0] > arr[1]:
            return 0

        # Check internal elements for peaks
        for i in range(1, n - 1):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                return i

        # If no internal peak, the last element must be a peak
        if arr[n - 1] > arr[n - 2]:
            return n - 1

        # This should ideally not be reached given the problem constraints
        return -1
