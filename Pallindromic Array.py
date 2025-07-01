# Your task is to complete this function
# Function should return true/false
def isPalinArray(arr):
    # Code here
    for i in arr:
        if(str(i)!=str(i)[::-1]):
            return 0
    return 1
