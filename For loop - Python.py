def multiplicationTable(N):
    #code here 
    li=[]
    m=1
    for i in range(1,11):
        m=N*i
        li.append(m)
        m=1
    for i in li:
        print(i,end=" ")
