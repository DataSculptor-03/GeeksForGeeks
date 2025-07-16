class Solution:
    def gcd(self, a : int, b : int) -> int:
        # code here
        if(1<=a and b<=10**9):
            while(b):
                a,b=b,a%b
            return a
