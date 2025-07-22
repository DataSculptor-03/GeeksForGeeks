class Solution:
    def getAreas(self, L , W , B , H , R):
        # code here
        if(1<=L<=10**4 and 1<=W<=10**4 and 1<=B<=10**4 and 1<=H<=10**4 and 1<=R<=10**4):
            a_r=L*W
            a_t=0.5*B*H
            a_c=3.14*(R)**2
            return int(a_r),int(a_t),int(a_c)
        
