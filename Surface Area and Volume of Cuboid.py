class Solution:
    def find(self, l, b, h):
        # Code here
        if(1<=l and b<=100 and h<=100):
            area=2*(l*b+b*h+h*l)
            volume=l*b*h
            return area,volume
