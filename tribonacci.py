modval = 10**9+7
def func(dp,n,k):
    if n==0:
        return 1 
    if n ==1 :
        return 1 
    if n==2:
        return 2
    if dp[n][k] != -1:
        return dp[n][k]
    ans =0
    ans =(func(dp,n-1,k)+func(dp,n-2,k)) % modval
    if k>0:
        ans += func(dp,n-3,k-1)
    ans %=modval
    dp[n][k] = ans 
    return ans 
dp = [[-1 for _ in range(k)] for _ in range(n)]
print(dp,n,k)
