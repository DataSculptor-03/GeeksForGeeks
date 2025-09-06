class Solution:
    def search(self,arr,key):
        # code here
        count=-1
        for i in range(len(arr)):
            if arr[i]==key:
                count=i
                break;
        if count==-1:
            return -1
        else:
            return count
