A,B=map(int,input().split())
l=list(map(int,input().split()[:A]))
for i in range(0,B):
  m=max(l)
  l.remove(m)
print(m)
