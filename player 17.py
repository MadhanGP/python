n1,n2=map(int,input().split())
num=1
while num>0:
    if num%n1==0 and num%n2==0:
        print(num)
        num=0
    else:
        num+=1
