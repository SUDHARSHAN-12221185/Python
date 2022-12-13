s=input()
l=len(s)
flag=False
start=0
end=l-1
while start<end:
    if s[start] != s[end]:
        flag=True
        break
    start+=1
    end-=1
if flag==True:
    print('not Palindrome')
else:
    print('Palindrome')