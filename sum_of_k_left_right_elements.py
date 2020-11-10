
#flipkart
a = [2,3,4,5,1,6,7,4,5,6]
k = 2
l = len(a)
b = [0]*l

for i in range(1,k+1):
    b[0]+=a[i%l]
print(b)
for i in range(1,k+1):
    b[0]+=a[(0-i)%l]
print(b)

    

for i in range(1,l):
    b[i]=b[i-1]
    b[i]-= a[i]
    b[i]+=a[i-1]
    b[i]+=a[(i+k)%l]
    b[i]-=a[(i-k-1)%l]
print(b)
