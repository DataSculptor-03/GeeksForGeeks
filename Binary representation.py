class Solution:
    def getBinaryRep(self, n):
        # code here
        s=0
        m=1
        while(n>0):
            rem=n%2
            s+=rem*m
            m*=10
            n//=2
        num=str(s).zfill(32)
        return num
