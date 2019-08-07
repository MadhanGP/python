def pro(l):
    p=1
    for i in l: 
        p=p*i
    return p 
    
print(pro(list(map(int,input().split()))))
