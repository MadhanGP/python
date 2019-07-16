limit=int(input())
li=list(map(str,input().split()[:limit]))
li.sort()
li.sort(key=len)
for i in li:
    print(i,end=" ")
