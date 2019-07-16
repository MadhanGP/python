N=int(input())
li=list(map(int,input().split()[:N]))
l=[]
for i in li:
    if li.count(i)>1:
        if i not in l:
            l.append(i)
            print(i,end=" ")
if len(l)==0:
    print('unique')
