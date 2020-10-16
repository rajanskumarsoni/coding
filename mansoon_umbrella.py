# mansoon umbrellas
# https://drive.google.com/drive/folders/1QT0T-YHFFmdWozfnT9vEIBsGvqA16wb4
def check(sizes,requirements):
    mem = []
    l =len(sizes)
    for i in range(l+1):
        mem.append([None]*(requirements+1))
        for j in range(requirements+1):
            if i==0:
                mem[i][j] = False
            if j ==0:
                mem[i][j] =True
            if i>0 and j>0:
                if sizes[i-1]<=j:
                    mem[i][j] = mem[i-1][j-sizes[i-1]] or mem[i-1][j]
                else:
                    mem[i][j]=mem[i-1][j]
    return mem[l][requirements]
    
sizes =[3,5,3] 
requirements = 0
def count(sizes,requirements):
    if check(sizes,requirements)== False:
        return -1 
    mem = []
    l =len(sizes)
    for i in range(l+1):
        mem.append([0]*(requirements+1))
        for j in range(requirements+1):
            if i==0:
                mem[i][j] = float('inf')
            if j ==0:
                mem[i][j] =0
            if i>0 and j>0:
                if sizes[i-1]<=j:
                    mem[i][j] = min(1+mem[i-1][j-sizes[i-1]], mem[i-1][j])
                else:
                    mem[i][j]=mem[i-1][j]
    return mem[l][requirements]
