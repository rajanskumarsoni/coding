def apoint(disc,low,parent,ap,d,i,ls):
    print(i,"wewe")
    global t 
    disc[i]=t 
    low[i] =t 
    t+=1
    c =0
    # print(t,disc)
    # if t >10:
    #     return
    for j in d[i]:
        if disc[j] ==-1:
            c+=1
            parent[j]=i
            apoint(disc,low,parent,ap,d,j,ls)
            low[i] = min(low[i],low[j])
            if low[j]>=disc[i]:
                if i<j:
                        ls.append((i,j))
                else:
                    ls.append((j,i))
                
            if parent[i]==-1 :
                if c>1:
                    ap[i]=1
                    
            else:
                if low[j]>=disc[i]:
                    ap[i]=1
                    

        elif parent[i] !=j:
            low[i]=min(low[i],disc[j])
            


n , m = map(int,input().split())
d = {i: [] for i  in range(n)}
for _ in range(m):
    s,e = map(int,input().split())
    d[e].append(s)
    d[s].append(e)
disc = [-1]*n
low = [-1]*n 
parent = [-1]*n 
ap = [-1]*n
t = 0
ls = []
for i in range(n):
    apoint(disc,low,parent,ap,d,i,ls)
c=sum(filter(lambda x: x==1,ap))
print(c)
for i in range(n):
    if ap[i] ==1:
        print(i)
print(len(ls))
ls.sort(key = lambda x: x[0])
ls.sort(key = lambda x: x[1])
for e in ls:
    print(e[0],e[1])

# print(ap,ls)
del t

