class Solution:
    def lengthString(self, str):
        #code here
        return len(str)
if __name__ =='__main__':
    tcs = int(input())
    
    for _ in range(tcs):
        s=input()
        
        print(Solution().lengthString(s))
        print("~")
