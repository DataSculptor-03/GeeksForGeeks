class Solution:
    def totalFine(self, date, car, fine):
        #Code here
        s=0
        if(date%2==0):
            for i in range(len(car)):
                if(car[i]%2!=0):
                    s+=fine[i]
        else:
            for i in range(len(car)):
                if(car[i]%2==0):
                    s+=fine[i]
        return s
    
