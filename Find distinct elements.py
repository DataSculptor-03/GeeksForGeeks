#User function Template for python3
def distinct(arr):
    # Your Code here
    s=set()
    for i in arr:
        if i not in s:
            s.add(i)
    return len(s)
