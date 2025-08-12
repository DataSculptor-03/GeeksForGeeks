#User function Template for python3
class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        s1 = ''
        for i in range(len(arr[0])):
            c = arr[0][i]
            for j in range(1, len(arr)):
                if i >= len(arr[j]) or c != arr[j][i]:
                    return s1  # stop immediately if mismatch
            s1 += c  # only add if all matched at index i
        return s1
