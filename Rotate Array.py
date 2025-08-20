#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        n=len(arr)
        d=d%n
        rotated=arr[d:]+arr[0:d]
        for i in range(n):
            arr[i]=rotated[i]
