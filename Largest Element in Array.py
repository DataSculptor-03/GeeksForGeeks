
from typing import List

class Solution:
    def largest(self, arr):
        # code here
        arr.sort()
        return arr[len(arr)-1]
