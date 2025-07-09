class Solution:
    def count (self,s):
        # your code here
        lc=0
        uc=0
        nc=0
        sc=0
        for i in s:
            if(i.isupper()):
                uc+=1
            elif(i.islower()):
                lc+=1
            elif(i.isnumeric()):
                nc+=1
            else:
                sc+=1
        return [uc,lc,nc,sc]
