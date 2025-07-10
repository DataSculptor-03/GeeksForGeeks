class Solution:
    # Function to find the maximum element from array arr1 and 
    # the minimum element from array arr2 and return their product.
    def find_multiplication(self, arr1, arr2):
        # code here
        arr1.sort()
        arr2.sort()
        p=arr1[len(arr1)-1]*arr2[0]
        return p
