#User function Template for python3

class Solution:
    def countWords(self,s):
        #code here
        count=0
        for i in s:
            if(i.isspace()):
                count+=1
        return count+1
