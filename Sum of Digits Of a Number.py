#User function Template for python3
class Solution:
    def sumOfDigits(self, n):
        '''
        :param n: given number
        :return: sum of digits of n.
        '''
        # code here
        s=0
        while(n>0):
            rem=n%10
            s+=rem
            n//=10
        return s
