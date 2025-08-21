class Solution:
    def inversionCount(self, arr):
        # Code Here
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums, 0
            
            mid = len(nums) // 2
            left, left_inv = merge_sort(nums[:mid])
            right, right_inv = merge_sort(nums[mid:])
            merged, merge_inv = merge(left, right)
            
            return merged, left_inv + right_inv + merge_inv

        def merge(left, right):
            merged = []
            i = j = inv_count = 0
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
                    inv_count += len(left) - i  # All remaining elements in left are > right[j]
            
            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged, inv_count

        _, count = merge_sort(arr)
        return count
