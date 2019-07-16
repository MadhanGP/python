limit=int(input())
array=[]
li_0=[]
count=0
for i in range(0,limit):
    array.extend(list(map(int,input().split()[:limit])))
for i in range(0,limit):
    li_0.append(0)
array.extend(li_0)
for j in range(0,limit**2):
    if array[j]==1 and array[j+1]==0 and array[j+limit]==0:
        count+=1 
print(count)
