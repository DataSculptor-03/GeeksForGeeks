class Solution:
    def sum_of_gp(self, n, a, r):
        # Code here
        if(1<=n and a<=10 and r<=10):
            if(r==1):
                return a*n
            else:
                return a*(r**n-1)//(r-1)
