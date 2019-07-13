num=int(input())
add=0
while num>0:
    last=num%10
    add+=last**2
    num=num//10
print(add)
