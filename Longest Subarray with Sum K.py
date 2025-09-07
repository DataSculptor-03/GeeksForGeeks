class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        prefix_sum = 0
        first_occurrence = {0: -1} 
        max_len = 0

        for i, num in enumerate(arr):
            prefix_sum += num

            if prefix_sum - k in first_occurrence:
                max_len = max(max_len, i - first_occurrence[prefix_sum - k])

            if prefix_sum not in first_occurrence:
                first_occurrence[prefix_sum] = i

        return max_len
