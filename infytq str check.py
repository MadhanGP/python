s=str(input())
res=''
for i in s:
    if i.isdigit() or i=='-':
        res+=i
print(int(res))
