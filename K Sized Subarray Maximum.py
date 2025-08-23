from collections import deque

class Solution:
    def maxOfSubarrays(self, arr, k):
        n = len(arr)
        q = deque()
        result = []

        for i in range(n):
            # Remove elements from front if they are out of the window
            if q and q[0] <= i - k:
                q.popleft()

            # Remove all elements smaller than the current from the back
            while q and arr[q[-1]] < arr[i]:
                q.pop()

            q.append(i)

            # Starting from index k-1, append max for current window
            if i >= k - 1:
                result.append(arr[q[0]])

        return result
