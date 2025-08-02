# Function to check if string
# starts and ends with 'gfg'
def gfg(S):
    b = S.lower()
    a="gfg"
    if (b.startswith(a) and b.endswith(a)):
        print("Yes")
    else:
        print("No")
