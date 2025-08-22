#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here 
        c=a+b
        s=set(c)
        l=list(s)
        l.sort()
        return l
