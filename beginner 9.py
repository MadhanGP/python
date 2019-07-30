n,k=map(int,input().split())
l=list(map(int,input().split()[:n]))
s=0
for i in range(k):
    s+=l[i]
print(s)
