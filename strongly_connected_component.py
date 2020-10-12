#code
from collections import deque
def foo(disc,low,instack,d,i,st):
    global t

    disc[i]=t
    low[i]=t
    t+=1
    st.append(i)
    instack[i]=True
  
    for j in d[i]:
       
        if disc[j] ==-1:
            foo(disc,low,instack,d,j,st)
            low[i] = min(low[i],low[j])
        elif instack[j]== True:
            
            low[i]=min(low[i],disc[j])

    if disc[i] == low[i]:
        while st[-1]!=i:
            
            a= st.pop()
            instack[a]=False
            
            print(a,end =" ")
        a = st.pop()
        instack[a]=False
     
        print(a,end="")
        print(",",end ="")
        
tm = int(input())
t =0
for _ in range(tm):
    n,m = map(int,input().split())
    ls = list(map(int,input().split()))
    d = {i:[] for i in range(n)}
    for i in range(0,2*m,2):
        d[ls[i]].append(ls[i+1])
    disc = [-1]*n
    low = [-1]*n
    instack = [False]*n
    st = deque()

    for i in range(n):
        # print(disc)
        if disc[i] ==-1:
            # print("njbn",i)
            foo(disc,low,instack,d,i,st)
  
    print()
    
    t =0
del t
