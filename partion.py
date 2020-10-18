https://docs.google.com/document/d/e/2PACX-1vRqsXE-Izz-qktbRKVexkt_eByPQQzaJ5vRKnd7gMClSINVRDF6tHJwXiVoz0NnJ-V9JamNaUvDEGou/pub
# citrix
n = 90
x =5
mem =[]
for i in range(n+1):
    mem.append([0]*(x+1))
    for j in range(x+1):
        if i ==0:
            mem[i][j] = 0
        if j ==0:
            mem[i][j] =1
        if i >0 and j >0:
            if i <=j:
                mem[i][j] = mem[i-1][j-(i)]+mem[i-1][j]
            else:
                mem[i][j] = mem[i-1][j]
print(mem[n][x])
