https://leetcode.com/discuss/interview-question/424497/harness-interview-question-how-to-solve-it

grid1 = [[1,0],[1,0],[0,1]]
grid2 = [[1,0],[1,0],[0,1]]
n  = len(grid1)
m = len(grid2[0])
def find(grid1,i,j,grid2,n,m):
    # print(i,j)
    # print(grid1[i][j],grid2[i][j])
    
    if i <0 or j<0 or i>= n or j>=m or (grid1[i][j] == grid2[i][j] and grid2[i][j]==0) or ( grid1[i][j] == grid2[i][j] and grid2[i][j]==2):
        
        return True
    if  grid1[i][j] != grid2[i][j] :
        return False
    grid2[i][j]=2 
    grid1[i][j]=2
    a = find(grid1,i-1,j,grid2,n,m)
    if a == False:
        return False
    a = find(grid1,i+1,j,grid2,n,m)
    if a == False:
        return False
    a = find(grid1,i,j-1,grid2,n,m)
    if a == False:
        return False
    a = find(grid1,i,j+1,grid2,n,m)
    if a == False:
        return False
    return True
c=0
for i in range(n):
    for j in range(m):
        if grid1[i][j]==1 :
            a = find(grid1,i,j,grid2,n,m)
            # print(a)
            if a == True:
                c+=1
print(c)
