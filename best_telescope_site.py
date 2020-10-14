# Question here
# https://drive.google.com/drive/folders/1wK3gjgD3cevq_7oXiJCJ9Z-nS4GxUwTm
''' Scientists want to select the best site to build
their new space observatory. The best site is defined as the city with the least ambient light from surrounding cities.
There are city_nodes cities numbered from 1 to city_nodes. The cities are connected by bidirectional edges to form a connected graph. The weight of each edge represents the distance between the connected cities. There is a distance Threshold that represents the minimum desired distance from any other city. Determine the city with the smallest number of neighboring cities that are nearer than the distance Threshold. If there are multiple answers, choose the higher city number.
Example distance Threshold $=3$ city_nodes $=3$ city_from $=[1,2]$ city_to $=[2,3]$ city_weight $=[3,1]$ '''

distance_threshold = 3
city_nodes = 3
city_from =[1,2]
city_to = [2,3]
city_weight =[3,1]
d ={i:[] for i in range(1,city_nodes+1)}
for a,b,c in zip(city_from,city_to,city_weight):
    d[a].append(c)
    d[b].append(c)
ind = 0
print(d)
m = float('inf')
for e in d:
    c=0
    for i in d[e]:
        if i <distance_threshold:
            c+=1 
    if c <=m:
        m =c 
        if e >ind:
            ind = e 
print(ind)
