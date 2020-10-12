import sys

# Write your code here
def road(low,disc,d,road_id,i,ls,parent):
        # pass
    global t 
    disc[i]=t
    low[i]=t 
    t+=1
    # if t >10:
    #     return
    for j in d[i]:
        if disc[j]==-1:
            parent[j]=i
            ls = road(low,disc,d,road_id,j,ls,parent)
            low[i] = min(low[i],low[j])
            if low[j]>disc[i]:
                # print("wew")
                ls.add(road_id[(i,j)])
        elif parent[i]!=j:
            # print("ewdwedew")
            low[i]=min(low[i],disc[j])
    return ls
t = 0
def main():
    n,m= map(int,input().split())
    d = {i:[] for i in range(1,n+1)}
    road_id = {}
    for i in range(1,m+1):
        a,b = map(int,input().split())
        d[a].append(b)
        d[b].append(a)
        road_id[(a,b)]=i
        road_id[(b,a)]=i

    low = [-1]*(n+1)
    disc = [-1]*(n+1)
    parent = [-1]*(n+1)
    
    ls =set()
    # print(d,road_id)
    # print(m,n)
    for i in range(1,n+1):
        if disc[i]==-1:
            road(low,disc,d,road_id,i,ls,parent)
    q = int(input())
    # print(ls)
    for _ in range(q):
        x = int(input())
        if x in ls:
            print("Unhappy")
        else:
            print("Happy")
import threading
if __name__=="__main__":
        main()

        sys.setrecursionlimit(10**6)

        threading.stack_size(10**8)

        t = threading.Thread(target=main)

        t.start()

        t.join()
        
