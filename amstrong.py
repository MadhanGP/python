num=int(input())
temp=num
add=0
while num>0:
    last=num%10
    add+=last**3
    num=num//10
if add==temp:
    print('yes')
else:
    print('no')
