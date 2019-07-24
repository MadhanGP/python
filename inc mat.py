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
if limit==2:
    for j in range(limit,(limit**2)+limit):
        if j==0:
            if array[j]==1 and array[j+1]==0 and array[j+limit]==0 and array[j+(limit+1)]==0:
                count+=1 
        elif j==limit-1:
            if array[j]==1 and array[j-1]==0 and array[j+limit]==0 and array[j+(limit-1)]==0:
                count+=1 
        elif j==(limit**2)-limit:
            if array[j]==1 and array[j+1]==0 and array[j-limit]==0 and array[j-(limit-1)]==0:
                count+=1 
        elif j==(limit**2)-1:
            if array[j]==1 and array[j-1]==0 and array[j-limit]==0 and array[j-(limit+1)]==0:
                count+=1
        if array[j]==1 and array[j+1]==0 and array[j-1]==0 and array[j+limit]==0 and array[j-limit]==0 and 
    
else:    
    for j in range(limit,(limit**2)+limit):
        if j==0:
            if array[j]==1 and array[j+1]==0 and array[j+limit]==0 and array[j+(limit+1)]==0:
                count+=1 
        elif j==limit-1:
            if array[j]==1 and array[j-1]==0 and array[j+limit]==0 and array[j+(limit-1)]==0:
                count+=1 
        elif j==(limit**2)-limit:
            if array[j]==1 and array[j+1]==0 and array[j-limit]==0 and array[j-(limit-1)]==0:
                count+=1 
        elif j==(limit**2)-1:
            if array[j]==1 and array[j-1]==0 and array[j-limit]==0 and array[j-(limit+1)]==0:
                count+=1
        else:    
            if array[j]==1 and array[j-1]==0 and array[j+1]==0 and array[j+limit]==0 and array[j-limit] and array[j-(limit+1)]==0 and array[j-(limit-1)]==0 and array[j+(limit-1)]==0 and array[j+(limit+1)]==0:
                count+=1 
print(count)


'''Input : 4
1 0 1 0 
1 1 0 0
0 0 0 0
1 1 0 0'''
