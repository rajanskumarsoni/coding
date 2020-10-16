# split the array 
# https://drive.google.com/drive/folders/1gT3RDRSRIqyrRg8JINAvJojocGgrEbag
def gcd(a,b):
    if b ==0:
        return a
    return gcd(b,a%b)
print(gcd(10,10))
arr = [3,5,1,7,8,20,14,28,22,361]
l =len(arr)
ls = [1]*(l+1)
ls[l] =0
for i in range(l)[::-1]:
    ls[i]=ls[i+1]+1
    for j in range(i+1,l)[::-1]:
        if gcd(arr[i],arr[j])>1 :
            ls[i]=min(ls[i],ls[j+1]+1)
            
          
print(ls)
        
