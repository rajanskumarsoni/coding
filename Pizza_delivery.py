# Question here https://imgur.com/a/DmOhAy4
# Pizza delivery boy
import math
def delivery(coord,speed):
    l= len(coord)
    m = 0
    for i in range(l):
        for j in range(i+1,l):
            d = math.sqrt((coord[i][0]-coord[j][0])**2+(coord[i][1]-coord[j][1])**2)
            if m<d:
                m =d 
    return "{0:.7}".format(m/speed)
print(delivery([[2,3],[3,4]],3))
