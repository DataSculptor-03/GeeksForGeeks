class Solution:
    def getMoreAndLess(self, arr, target):
        # code here
        count1=0
        count2=0
        for i in range(0,len(arr)):
            if(arr[i]<=target):
                count1+=1
        for i in range(0,len(arr)):
            if(arr[i]>=target):
                count2+=1
        return count1,count2
