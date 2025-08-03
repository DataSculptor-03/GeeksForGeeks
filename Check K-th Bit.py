class Solution:
    def checkKthBit(self, n, k):
        s = ''
        while n > 0:
            rem = n % 2
            s += str(rem)
            n //= 2
        if k >= len(s):
            s += '0' * (k - len(s) + 1)
        return s[k] == '1'
