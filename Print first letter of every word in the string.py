class Solution:
    def firstAlphabet(self, S):
        # code here
        s=''
        word=S.split()
        for i in word:
            s+=i[0]
        return s
