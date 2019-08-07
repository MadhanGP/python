def pal(s):
    r=s[::-1]
    if r==s:
        return True
    else:
        return False

string=str(input())
l=[]
for i in string:
    l.append(i)
while(pal(l)):
    l.pop()
for i in l:
    print(i,end='')
