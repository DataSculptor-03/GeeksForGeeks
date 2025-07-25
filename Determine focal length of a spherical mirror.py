import math
class Solution:
    def findFocalLength(self, R, type):
        # Code here
        if(1<=R<=100):
            if(type=="concave"):
                c=R/2
                return math.floor(c)
            elif(type=="convex"):
                c=R/2
                return math.floor(-c)
