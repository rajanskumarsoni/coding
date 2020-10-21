# question https://docs.google.com/document/d/e/2PACX-1vSjEnRqU37XNgXA8Eo90yJD3Zi5piHEMDjk5E_MiN7GukMd5D_mfrQ2TxdV-FI9nHzc0BALzT52rWu0/pub?fbclid=IwAR0TqjjvSligdp1VmBz_jt5vq5REb8B_3xHT5s2JkCTp5c27XrNUqUOlxS0
# dgraph
arr = [20,40,100]
dic ={}
ans =0
for e in arr:
    # if e%60 ==0:
    #     if 0 in dic :
    #         ans+=dic[0]
    #         dic[0]+=1
    #     else:
    #         dic[0]=1 
    # else:
        a = 60 - (e%60)
        if a in dic:
            ans+=dic[a]
        if   e%60 not in dic: 
        
            
            dic[e%60]=1
        else:
            
            dic[e%60]+=1
# print(dic)
print(ans)
