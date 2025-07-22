import math
class Solution:
    def distance(self, x1, y1, x2, y2):
        # Code here
        if -1000 <= x1 <= 1000 and -1000 <= y1 <= 1000 and -1000 <= x2 <= 1000 and -1000 <= y2 <= 1000:
            c = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        if(c>=math.floor(c)+0.5):
            return math.ceil(c)
        else:
            return math.floor(c)
