#User function Template for python3

class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        # code here
        arr=arr1+arr2
        arr.sort()
        m=len(arr)//2
        s=arr[m-1]+arr[m]
        return s
