# Function should return an integer value
class Solution:
    def convertFive(self, n):
        # Code here
        n1=str(n)
        n1=n1.replace('0','5')
        return (int)(n1)
                
