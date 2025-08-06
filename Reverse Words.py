class Solution:
    def reverseWords(self, s):
        # code here
        word=s.split()
        return ' '.join(word[::-1])
