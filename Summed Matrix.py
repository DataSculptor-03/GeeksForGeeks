class Solution:
    def sumMatrix(self, n, q):
        # code here 
        low = max(1, q - n)
        high = min(n, q - 1)

        count = max(0, high - low + 1)

        return count
