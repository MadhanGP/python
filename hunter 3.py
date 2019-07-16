N=int(input())
li=list(map(int,input().split()[:N]))
for i in range(0,N):
    if li[i]==i:
        print(i,end=" ")
