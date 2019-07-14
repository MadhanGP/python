limit=int(input())
string=input('')
l=list(string)
v=['a','e','i','o','u']
for i in l:
    if i in v:
        l.remove(i)
rev=l[::-1]
s=''.join(rev)
print(s)
