s=input('Enter Roman number: ')
def romantointeger(s):
    d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'i':1,'v':5,'x':10,'l':50,'c':100,'d':500,'m':1000}
    ans=0
    for i in range(len(s)):
        if i+1!=len(s) and d[s[i]] <  d[s[i+1]]:
            ans-=d[s[i]]
        else:
            ans+=d[s[i]]
    return ans
print('Roman in Integer is',romantointeger(s))
