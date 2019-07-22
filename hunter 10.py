N=int(input())
M=int(input())
A=set(map(int,input().split()[:N]))
B=set(map(int,input().split()[:M]))
C=B-A
if len(C)==0:
    print("YES")
else:
    print("NO")
