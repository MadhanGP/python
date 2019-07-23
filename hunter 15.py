n=int(input())
l=list(map(int,input().split()[:n]))
superstar=max(l)
while len(l)!=0:
    m=max(l)
    print(m,end=" ")
    r=l.index(m)
    l=l[r+1:]
print('\n',superstar)
