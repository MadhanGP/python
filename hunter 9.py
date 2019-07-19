N=int(input())
li=list(map(int,input().split()[:N]))
for i in range(0,N):
    for j in range(i+1,N):
        if li[i]+li[j]>-1 and li[i]+li[j]<1:
            print(li[i],li[j])
