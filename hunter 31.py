def product(l):
    p=1
    for i in l:
        p=p*i
    return p


n=int(input())
l=list(map(int,input().split()[:n]))
s1=[]
for i in range(n):
    s=product(l[i:n+1])
    s1.append(s)
rev=l[::-1]
for i in range(n):
    s=product(rev[i:n+1])
    s1.append(s)
print(max(s1))
