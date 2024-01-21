def climbStairs(self, n):
        
    if n==1:
        return 1
    elif n==2:
        return 2

    arr=[1 for i in range(n)]
    arr[1]=2
    for i in range(1,n-1):
        arr[i+1]=arr[i]+arr[i-1]
    return arr[n-1]