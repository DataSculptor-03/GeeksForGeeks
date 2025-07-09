class Solution:
    def valueEqualToIndex(self, arr):
        li=[]
        for i in range(0,len(arr)):
            if(i+1==arr[i]):
                li.append(i+1)
        return li
