class Solution:
    def pattern(self, N):
        # code here
        if(-10**5<=N<=10**5):
            result=[]
            temp=N
            while(temp>0):
                result.append(temp)
                temp-=5
            result.append(temp)
            while(temp<N):
                temp+=5
                result.append(temp)
            return result
