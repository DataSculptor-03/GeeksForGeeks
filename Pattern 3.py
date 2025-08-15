class Solution:
    def printTriangle(self, N):
        if(1<=N<=100):
            for i in range(1,N+1):
                for j in range(1,i+1):
                    print(j,end=" ")
                print()
