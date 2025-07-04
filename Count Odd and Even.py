class Solution:
    def countOddEven(self, arr):
        #Code here
        c1=0
        c2=0
        for i in range(len(arr)):
            if(arr[i]%2==0):
                c1+=1
            else:
                c2+=1
        return c2,c1
