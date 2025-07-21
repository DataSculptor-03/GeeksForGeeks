class Solution:
    def sum_of_square_evenNumbers(self, n):
        # Code here
        if(1<=n<=10000):
            s=4*(n*(n+1)*(2*n+1))//6
        return s
