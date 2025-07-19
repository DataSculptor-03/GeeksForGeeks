class Solution:
    def greatestOfThree(self,A,B,C):
        #code here
        if(10**(-9)<=A,B,C<=10**9):
            if(A>B and A>C):
                return A
            elif(B>A and B>C):
                return B
            else:
                return C
