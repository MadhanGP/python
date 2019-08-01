n=int(input())


f1,f2=1,1 
f=[]
f.append(f1)
f.append(f2)
for i in range(0,n):
    f3=f1+f2
    f1=f2
    f2=f3
    f.append(f3)

p=[]
count=0
for i in range(2,1000):
    if count<=n:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            p.append(i)
            count+=1

#print(f)
#print(p)
if n%2!=0:
    o=(n-1)/2
    print(f[int(o)])
    
else:
    e=(n-2)/2
    print(p[int(e)])
    
