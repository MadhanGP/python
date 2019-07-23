n=int(input())
l=[]
for i in range(n):
  a=input('')
  l.append(a)
li=[]
for j in zip(*l):
  if (j.count(j[0])==len(j)):
    li.append(j[0])
  else:
    break
print("".join(li))
