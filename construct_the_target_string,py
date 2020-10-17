# // python Program to Count the number of ways to 
# // construct the target string 


dp = [[-1 for i in range(100)] for j in range(100)]
# print(len(dp))
mod = 1000000007
def calculate(pos,prev,s,index):
    global dp
    global mod
    if pos == len(s):
        return 1
    if dp[pos][prev]!=-1 :
        return dp[pos][prev]
    a = ord(s[pos]) - ord('a')
    ans =0
    for i in index[a]:
        if i >prev:
            ans=(ans%mod+calculate(pos+1,i,s,index)%mod)%mod
    dp[pos][prev] =ans 
    return ans
def countWays(s,ls):
    index = [[] for i in range(26)]
    # l = len(ls[0])
    for e in ls:
        for i,c in enumerate(e):
            index[ord(c)-ord('a')].append(i+1)
    # print(index)
    return calculate(0,0,s,index)
ls = ["afsdc","aeeeedc","ddegerg"]
s ="ae"
# print(dp)    
print(countWays(s,ls))
