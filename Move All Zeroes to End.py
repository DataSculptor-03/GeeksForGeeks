class Solution:
    def pushZerosToEnd(self,arr):
        # code here
        non_zero=0
        for i in range(0,len(arr)):
            if(arr[i]!=0):
                arr[non_zero]=arr[i]
                non_zero+=1
        for i in range(non_zero,len(arr)):
            arr[i]=0
               
