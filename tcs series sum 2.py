n=int(input())
r1,r2=3,4
s1,s2=0,0
print(s1,end=" ")
print(s2,end=" ")
for i in range(n):
  if i%2!=0:
    s1=s1+r1
    print(s1,end=" ")
  else:
    s2=s2+r2
    print(s2,end=" ")
