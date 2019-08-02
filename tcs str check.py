n=int(input())
s=str(n)
sl=[]
count=0
for i in s:
    sl.append(i)
#print(sl)
for num in range(1,n):
    st=str(num)
    check=[]
    for j in st:
        check.append(j)
    c=0
    #print(check)
    for k in check:
      if k in sl:
        c+=1
    if c==len(check):
      count+=1
print(count)
