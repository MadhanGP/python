n=int(input())
l=list(map(int,input().split()[:n]))
temo_list=l
while len(l)>1:
    a=[]
    for i in range(1,len(l),2):
        a.append(l[i])
    l=a
for i in l:
    print(temo_list.index(i))
