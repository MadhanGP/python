num=int(input())
fact=1
if num==0:
    print(fact)
else:
    for i in range(2,num+1):
        fact*=i
    print(fact)
