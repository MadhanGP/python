limit=int(input())
word=sorted('kabali')
count=0
for i in range(limit):
    name=input('')
    a=sorted(name)
    if word==a:
        count+=1 
print(count)
