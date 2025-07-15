class Solution:
    def reciprocalString(self, S):
        # code here
        s=''
        for i in S:
            if(i.isalpha()):
                c=ord(i)
                if(c>=65 and c<=90):
                    s1=chr(90-(c-65))
                    s+=s1
                elif(c>=97 and c<=122):
                    s1=chr(122-(c-97))
                    s+=s1
            else:
                s+=i
        return s
                
