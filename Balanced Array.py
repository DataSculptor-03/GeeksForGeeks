class Solution:
    # Function to find the minimum value required to balance the array.
    def min_value_to_balance(self, arr):
        # code here
        s1=0
        s2=0
        for i in range(0,len(arr)//2):
            s1+=arr[i]+arr[len(arr)//2-i]
        for i in range(len(arr)//2,len(arr)):
            s2+=arr[i]+arr[len(arr)-i]
        return abs(s1-s2)
