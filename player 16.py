num=int(input())
li=list(map(int,input().split()[:num]))
for i in li:
    if li.count(i)==1:
        print(i)
