N=int(input())
li=list(map(int,input().split()[:N]))
for i in range(0,N):
    if li.count(i)>1:
        print(i)
        break
else:
    print('unique')
