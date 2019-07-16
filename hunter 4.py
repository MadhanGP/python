N=int(input())
li=list(map(int,input().split()[:N]))
for i in li:
    if li.count(i)==1:
        print(i,end=" ")
