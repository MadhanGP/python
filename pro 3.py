x,y=map(str,input('').split())
l=[]
l.append(x)
l.append(y)
s=[]
for i in zip(*l):
    print(i)
    if i.count(i[0])==len(i):
        s.append(i[0])
    else:
        break
m=max(l,key=len)
k=len(m)-len(s)
print(k)
