f,l=map(int,input().split())
for num in range(f+1,l):
    if num>0:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)
