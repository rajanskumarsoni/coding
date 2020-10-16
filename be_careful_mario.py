# question https://imgur.com/a/Xyqf3Wo
import math
rn = 10
a = math.sqrt(rn)
prime =[-1]*rn
for i in range(2,int(a)+1):
    if prime[i]==-1:
        for j in range(i*i,rn,i):
            prime[j] =0
c=0
for i in range(2,rn):
    if prime[i]==-1:
        c+=1 
    prime[i]=c
print(prime)

def foo(r1,r2,n,s):
    global prime
    if s[n-1]=='#' or s[0]=='#':
        return "No way!"
    s[n-1]=0
    for i in range(n)[::-1]:
        if s[i]=="*":
            a =float('inf')
            if i+1<n and s[i+1] != '#':
                a = 1+s[i+1]
            b =float('inf')
            if i+2<n and s[i+2] !='#':
                b = 1+s[i+2]
            c=float('inf')
            if i >=2 and prime[i]/i >= r1/r2  and i+prime[i]<n and s[i+prime[i]] != '#':
                c = 1+s[i+prime[i]]
            # print(s)
            s[i] = min(a,b,c)
    print(s)
    return s[0]
                
        
    
t = 1   
s="*#**#*****"
r1 =1 
r2 =2
n =10
s=list(s)
# t = int(input())
for _ in range(t):
    # r1,r2 = map(int, input().split())
    # n = int(input())
    # s = input()
    # s=list(s)
    
    print(foo(r1,r2,n,s))
