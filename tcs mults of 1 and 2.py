n=int(input())
l=[]
s1,s2=0,0
r1,r2=1,2 
l.append(s1)
l.append(s2)
for i in range(1,n+1):
    if i%2==0:
        s1=s1+r1
        l.append(s1)
    else:
        s2=s2+r2
        l.append(s2)
#print(l)
print(l[n-1])
