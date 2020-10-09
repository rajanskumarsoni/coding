# https://imgur.com/a/qBLtQSk

#cv = current value
#fv = futute value
#s = saving
def foo(cv,fv,s):
    v = []
    w =[]
    l =len(cv)
    for i in range(l):
        if fv[i]-cv[i] >0:
            v.append(fv[i]-cv[i])
            w.append(cv[i])
    l = len(v)
    mem = []
    for i in range(l+1):
        mem.append([0]*(s+1))
        for j in range(s+1):
            if i ==0:
                mem[i][j] =0
            if j ==0:
                mem[i][j] =0
            if i>0 and j>0:
                if w[i-1]<=j:
                    mem[i][j] = max(v[i-1]+mem[i-1][j-w[i-1]],mem[i-1][j])
                else:
                    mem[i][j] = mem[i-1][j]
    return mem[l][s]
    
    
cv = [175,133,109,210,97]
fv =[200,125,128,228,133]
s = 250
print(foo(cv,fv,s))
        
