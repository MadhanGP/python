r,c=map(int,input().split())
m=[]
for i in range(r):
    a=list(map(int,input().split()[:c]))
    m.append(a)
row=[1]*r
col=[1]*c
for i in range(r):
    for j in range(c):
        if m[i][j]==0:
            row[i]=0
            col[j]=0
for i in range(r):
    for j in range(c):
        if row[i]==0 or col[j]==0:
            m[i][j]=0
for i in m:
    print(*i)
