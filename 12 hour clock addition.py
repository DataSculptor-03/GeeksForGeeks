class Solution:
    def clockSum(self, num1, num2):
        # code here
        res=num1%12+num2%12
        if(res>11):
            return (res-12)
        else:
            return res
