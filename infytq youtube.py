s=input()
a=s.split(',')
d=''
l=[]
for i in a:
    b=i.split(':')
    name=b[0]
    num=str(b[1])
    sq=0
    for j in num:
        sq=sq+(int(j)*int(j))
    if sq%2==0:
        d+=name[-1]
        d+=name[0:-1]
    else:
        temp1=name[0]
        temp2=name[1]
        name=name[2:]
        d=name+temp1+temp2
    l.append(d)
print(*l,sep=',')
