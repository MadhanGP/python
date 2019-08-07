n=int(input())
l=list(map(int,input().split()[:n]))
r=l[::-1]
print(*r,sep='->')
