class Solution:
    def nthTermOfAP(self, a1 : int, a2 : int, n : int) -> int:
        # code here
        if((-(10**4)<=a1) and (a2<=10**4) and (1<=n<=10**4)):
            val=a1+(n-1)*(a2-a1)
        return val
