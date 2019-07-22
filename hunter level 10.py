n=int(input())
m=int(input())
A=set(map(int,input().split()[:n]))
B=set(map(int,input().split()[:m]))
C=B-A
if len(C)==0:
    print("YES")
else:
    print("NO")
