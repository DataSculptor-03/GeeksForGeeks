import math
class Solution:
    def getCompundInterest(self, P ,T , N , R):
        # code here
        if(1<=P<=1000 and 1<=T<=20 and 1<=N<=4 and 1<=R<=20):
            ci=P*((1+(R/(100*N)))**(N*T))
            return math.floor(ci)
        else:
            ci=P*((1+(R/(100*N)))**(N*T))
            return math.floor(ci)
