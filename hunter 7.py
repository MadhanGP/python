N=int(input())
li=list(map(int,input().split()[:N]))
for i in range(0,N):
    if i%2==0 and li[i]%2!=0:
        print(li[i],end=" ")
    elif i%2!=0 and li[i]%2==0:
        print(li[i],end=" ")
