n=int(input())
l=list(map(int,input().split()[:n]))
l.sort()
m=l[::-1]
for i in m:
    print(i,end="")
