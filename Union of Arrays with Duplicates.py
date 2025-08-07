class Solution:    
    def findUnion(self, a, b):
        # code here
        set1=set(a)
        set2=set(b)
        set3=set1.union(set2)
        return len(set3)
