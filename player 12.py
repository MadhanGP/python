a,b=map(int,input().split())
l=list(map(int,input().split()[:a]))
for i in (0,b):
    l=[l[-1]]+l[:-1]
for j in l:
    print(j,end=' ')
