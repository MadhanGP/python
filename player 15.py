name=input('')
count=0
for i in name:
    if name.count(i)>count:
        count=name.count(i)
        g=i
print(g)
