def prime(a):
    for j in range(2,a):
        if a%j==0:
            break
    else:
        if a!=1:
            print(a,end=" ")
        
num=int(input())
for i in range(1,num+1):
    if num%i==0:
        prime(i)
