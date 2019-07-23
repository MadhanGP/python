l=list(map(str,input().split()))
s=[]
for i in zip(*l):
  if i.count(i[0])==len(i):
      s.append(i[0])
  else:
    break
k=len(l[1])-len(s)
print(k)
