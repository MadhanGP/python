n=int(input())
l=list(map(int,input().split()[:n]))
s1=[]
for i in range(n):
    s=sum(l[i:n+1])
    s1.append(s)
rev=l[::-1]
for i in range(n):
    s=sum(rev[i:n+1])
    s1.append(s)
print(max(s1))
