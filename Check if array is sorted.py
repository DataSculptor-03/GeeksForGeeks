class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        # code here
        c = arr.copy()           # original array
        sorted_arr = sorted(arr) # non-destructive sorting
        if c == sorted_arr:
            return 1
        else:
            return 0
