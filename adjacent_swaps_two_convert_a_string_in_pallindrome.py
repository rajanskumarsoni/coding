# Minimum adjacent swaps two convert a string in pallindrome
# https://medium.com/@molchevsky/best-solutions-for-microsoft-interview-tasks-min-swaps-to-make-palindrome-e931689f8cae
# https://leetcode.com/discuss/interview-question/351783/



def exist(string,s,e):
    
    for i in range(s+1,e)[::-1]:
        if string[s] ==string[i]:
            return i
    return -1
        
def count(string,l):
    s = 0
    e = l-1
    c =0
    while s<=e :
        if string[e] == string[s]:
            e-=1 
            s+=1 
        else:
            a = exist(string,s,e)
            if a == -1:
                string[s],string[s+1] = string[s+1],string[s]
                c+=1
            else:
                
                for k in range(a,e):
                    string[k],string[k+1] = string[k+1],string[k]
                    c+=1
            e-=1 
            s+=1
                
    return c
            
                
def ispallindromic(s):
    l= len(s)
    s = list(s)
    ls =[0]*26
    for e in s:
        ls[ord(e)-ord('a')]+=1
    c =0
    for e in ls:
        if e %2 ==1:
            c+=1
        if c >1:
            return -1
    return count(s,l)
print(ispallindromic("abcccca"))
