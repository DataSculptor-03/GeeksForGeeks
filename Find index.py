#User function Template for python3

arr = tuple(map(int, input().split()))
x = int(input())

########### Write your code below ###############
# Print the index of x in arr
l=list(arr)
for i in range(len(l)):
    if l[i]==x:
        print(i)
        break;
########### Write your code above ###############
