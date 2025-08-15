from typing import List


class Solution:
    def minimumTime(self, N : int, cur : int, pos : List[int], time : List[int]) -> int:
        # code here
        li=[]
        for i in range(0,N):
            diff=abs(cur-pos[i])
            cal=diff*time[i]
            li.append(cal)
        li.sort()
        return li[0]
        
