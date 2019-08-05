def pal(n,c):
    
    temp=n
    s=str(n)
    rev=s[::-1]
    rev_int=int(rev)
    if temp!=rev_int:
        n=temp+rev_int
        p= 0
        c+=1
    else:
        p= 1
    if p==0:
        pal(n,c)
        
    else:
        print(n)
        print(c)
n=int(input())
c=0
p=pal(n,c)


#alternate and correct
def pal(i):
    if str(i)==str(i)[::-1]:
        return False
    else:
        return True
n=int(input())
n=n+int(str(n)[::-1])
while(pal(n)):
    n=n+int(str(n)[::-1])
print(n)
