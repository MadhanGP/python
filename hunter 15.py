n=int(input())
l=list(map(int,input().split()[:n]))
superstar=max(l)
s=[]
while len(l)!=0:
    m=max(l)
    s.append(m)
    r=l.index(m)
    l=l[r+1:]
print(*s)
print(superstar)
