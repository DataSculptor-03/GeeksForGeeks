class Solution:
    def missingRange(self, arr, low, high):
        #code here
        arr_set = set(arr) 
        l = []
        for i in range(low, high + 1):
            if i not in arr_set:
                l.append(i)
        return l
