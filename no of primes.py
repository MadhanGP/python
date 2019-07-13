f,l=map(int,(input().split()))
count=0
for num in range(f,l+1):
    if num>0:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            count+=1 
print(count)
