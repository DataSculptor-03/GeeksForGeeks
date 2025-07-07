class Solution:
    def findIndex(self, arr, x):
        #code
        index=-1
        for i in range(len(arr)):
            if(arr[i]==x):
                index=i+1
        return index
