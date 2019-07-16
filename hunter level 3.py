N=int(input())
li=list(map(int,input().split()[:N]))
l=[]
for i in range(0,N):
    if li[i]==i:
        l.append(i)
        print(i,end=" ")
if len(l)==0:
    print(-1)
