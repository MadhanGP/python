f,l=map(int,input().split())
for num in range(f+1,l):
    temp=num
    add=0 
    while num>0:
        last=num%10
        add+=last**3
        num=num//10
    if add==temp:
        print(temp)
