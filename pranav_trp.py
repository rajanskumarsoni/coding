# question here https://imgur.com/a/6WzCwLM

s = "[[[][[]][]]]"
from collections import deque
q= deque()
q.append('[')
for e in s[1:]:
    print(q)
    
    if e == ']':
        s=0
    
        while q[-1] != '[':
            a= q.pop()
            s+=a
        q.pop()
        if s==0:
            q.append(1)
        else:
            q.append(2*s)
        
    else:
        q.append('[')
print(q[0])
