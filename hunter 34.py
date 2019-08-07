n=int(input())
s=str(n)
s_l=[]
for i in s:
    s_l.append(i)
s_l.sort()
flag=0
for num in range(n+1,10000):
    st=str(num)
    l=[]
    for i in st:
        l.append(i)
    l.sort()
    if l==s_l:
        print(num)
        flag=1
        break
if flag==0:
    print('impossible')
