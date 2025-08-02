# Function to print x in increasing order
def printIncreasingPower(x):
    ##Your code here
    
    # Loop to jump in powers of 2
    i=1
    res=0
    while(i*i<=x):
        ##Your code here
        res=i*i
        print (res, end = " ")
        i+=1
        
        ##Your code here
