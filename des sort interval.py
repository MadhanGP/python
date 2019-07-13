n=int(input())
l=list(map(int,input().split()[:n]))
l.sort()
m=l[::-1]
if n==0:
    print('0')
else:
    for i in m:
        print(i,end="")
