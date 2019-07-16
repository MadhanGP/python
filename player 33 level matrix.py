limit=int(input())
array=[]
a=[]
for i in range(0,limit):
    a.append(0)
array.extend(a)
li_0=[]
count=0
for i in range(0,limit):
    array.extend(list(map(int,input().split()[:limit])))
for i in range(0,limit):
    li_0.append(0)
array.extend(li_0)
for j in range(limit,(limit**2)+limit):
    if array[j]==1 and array[j-1]==0 and array[j+1]==0 and array[j+limit]==0:
        count+=1 
print(count)
