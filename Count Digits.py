class Solution:
    def evenlyDivides(self, n):
        # code here
        count=0
        temp=n
        while(n>0):
            r=n%10
            if(r!=0 and temp%r==0):
                count+=1
            n//=10
        return count 
