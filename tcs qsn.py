n=int(input())
l=[]
for i in range(n):
    a=str(input())
    l.append(a)
for j in l:
    print("".join(sorted(j)))
