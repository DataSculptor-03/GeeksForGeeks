class Solution:
    def countFreq(self, arr, target):
        #code here
        c=0
        for i in arr:
            if i==target:
                c=arr.count(i)
                break;
            else:
                c=0
        return c
