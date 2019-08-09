s=str(input())
add=0
for i in s:
    n=int(i)
    add+=n
string=str(add)
l=[]
for i in string:
    l.append(i)
rev=l[::-1]
if rev==l:
    print('YES')
else:
    print('NO')
