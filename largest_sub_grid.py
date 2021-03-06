#############For question description look at below link
# https://imgur.com/a/qBLtQSk
############For maxsumgrid function watch below video
# https://www.youtube.com/watch?v=WxjYE4_agbo&ab_channel=PrakashShukla

grid = [[2,2,2],[3,3,3],[4,4,4]]

def maxsumgrid(dp,k,l):
    m = 0
    for i in range(k,l+1):
        for j in range(k,l+1):
            a = dp[i][j]-(dp[i-k][j]+dp[i][j-k])+dp[i-k][j-k]
            if a>m:
                m =a
    return m
def search(grid,mxval):
    l = len(grid)
    dp = [[0 for _ in range(l+1)] for _ in range(l+1)]
    for i in range(1,l+1):
        for j in range(1,l+1):
            dp[i][j] = grid[i-1][j-1]-dp[i-1][j-1]+dp[i-1][j]+dp[i][j-1]
    s = 1 
    e = l
    m = s+(e-s)//2
    size =0
    while s<= e:
        
        a = maxsumgrid(dp,m,l)
        if a<=mxval:
            size = m 
            s = m+1 
            m = s+(e-s)//2
        else:
            e = m-1
            m = s+(e-s)//2
    return size
    
print(search(grid,3))
