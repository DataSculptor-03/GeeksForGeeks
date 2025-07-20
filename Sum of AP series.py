class Solution:
    def sum_of_ap(self, n, a, d):
        # Code here
        if(1<=n and a,d<=10000):
            ans=(n*((2*a)+(n-1)*d))//2
        return ans
