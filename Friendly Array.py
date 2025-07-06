class Solution:
    def calculateFriendliness(self, arr):
        s=0
        for i in range(0,len(arr)):
            if(i==len(arr)-1):
                s=s+abs(arr[len(arr)-1]-arr[0])
            else:
                s=s+abs(arr[i]-arr[i+1])
        return s
