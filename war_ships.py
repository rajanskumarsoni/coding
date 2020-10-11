# war ship
# Asked herer  https://imgur.com/a/DmOhAy4
from collections import deque
def number_of_ships(m,l):
    q=deque()
    
    q.append((2,1))
    c =1
    while len(q)>0:
        a = q.popleft()
        # print(a)
        if a[1] < l:
            n = a[0]*a[0]+1
            n = n %m
            c+=n
            
            for i in range(n):
                q.append((i,a[1]+1))
    return c%m
    
print(number_of_ships(7,8))
    
