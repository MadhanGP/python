r1,r2=3,4
s1,s2=1,1
l=
n=int(input())
for i in range(1,n+1):
    if i%2!=0:#oddplaces
        s1=s1*r1
        print(s1,end=" ")
    else:
        s2=s2*r2
        print(s2,end=" ")
