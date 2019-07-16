sym=input('')
count=0
for i in sym:
    if i=='(':
        count+=1 
    elif i==')':
        count-=1 
if count==0:
    print('yes')
else:
    print('no')
