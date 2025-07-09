class Solution:
    def removeSpecialCharacter (self, S):
        #code here
        a=[]
        for i in S:
            if(i.isalpha()):
                a.append(i) 
        final=''.join(a)
        if final=="":
            return -1
        else:
            return final                
