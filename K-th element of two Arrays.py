class Solution:

    def kthElement(self, a, b, k):
        pass
        arr=a+b
        arr.sort()
        return arr[k-1]
