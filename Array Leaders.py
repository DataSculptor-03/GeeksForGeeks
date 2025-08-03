class Solution:
    def leaders(self, arr):
        # code here
        li = []
        max_from_right = float('-inf')
        for i in reversed(arr):
            if i >= max_from_right:
                li.append(i)
                max_from_right = i
        return li[::-1]
