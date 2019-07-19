N=int(input())
li=list(map(int,input().split()[:N]))
for i in range(0,N):
    for j in range(i+1,N):
        for k in range(N):
            if li[i]+li[j]==li[k] and i<j<k:
                print(li[i],li[j],li[k])
