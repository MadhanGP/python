def numofpaths(m,n):
    if (m==1 or n==1):
        return 1
    else:
       return numofpaths(m-1,n)+numofpaths(m,n-1)
        
m=int(input())
n=int(input())
print(numofpaths(m,n))
