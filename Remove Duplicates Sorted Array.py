class Solution:
    def removeDuplicates(self, arr):
        seen = set()
        index = 0
        for i in arr:
            if i not in seen:
                seen.add(i)
                arr[index] = i  # Place unique element at correct position
                index += 1
        return index  # Return number of unique elements
