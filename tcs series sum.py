r1,r2=2,3
s1,s2=1,1
n=int(input())
l=[]
#print(s1,end=" ")
l.append(s1)
#print(s2,end=" ")
l.append(s2)
for i in range(1,n):
    if i%2!=0:#oddplaces
        s1=s1*r1
        l.append(s1)
        #print(s1,end=" ")
    else:
        s2=s2*r2
        l.append(s2)
        #print(s2,end=" ")
print(l)
print(l[n-1])
