n=int(input())
l=list(map(int,input().split()[:n]))
l.sort()
m=l[::-1]
if l.count(0)==len(l):
    print(0)
else:
    for i in m:
        print(i,end="")
