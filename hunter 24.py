n,k=map(int,input().split())
l=list(map(int,input().split()[:n]))
flag=0
for i in range(0,n):
    for j in range(i+1,n):
        if l[i]+l[j]==k:
            flag=1
if flag==1:
    print("YES")
else:
    print("NO")
