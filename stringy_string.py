def finf_cost(ls,size):
    mid= size//2
    if size%2==0:
        median=(ls[mid-1]+ls[mid])//2
    else:
        median = ls[mid]
    cost =0
    for i in range(size):
        cost+=abs(median-ls[i])
    return cost
s = ["chakshu","pekku","punk","golem","tyagi"]
n=5
min_string, max_string = "",""
min_cost,max_cost = 2**31-1,0
ls =[]
for i in range(n):
    t = s[i]
    cost =0
    for j in range(len(t)):
        cost+=(ord(t[j])-ord('a'))+1 
    # print(i)
    ls.append(cost)
    if cost>max_cost:
        max_cost=cost
        max_string =t
    if cost<min_cost:
        min_cost=cost
        min_string=t
l=len(ls)
ls1 =ls[:l-1]
ls2=ls[1:]
ls.sort()
cost1 =finf_cost(ls1,n-1)
cost2 = finf_cost(ls2,n-1)
if cost1<cost2:
    print(max_string)
else:
    print(min_string)
