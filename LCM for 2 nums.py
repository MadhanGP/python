'''a=int(input())
b=int(input())
c=max(a,b)
#print(c)
while True:
    if c%a==0 and c%b==0:
        print(c)
        break
    else:
        c=c+1'''

l=list(map(int,input().split()))
c=max(l)
for i in l:
  if c%i==0:
    print(c)
  else:
    c=c+1
