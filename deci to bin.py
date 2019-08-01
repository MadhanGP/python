def decimaltobinary(num):
    q=[]
    while num>=1:
        qu=num%2
        num=num//2
        q.append(qu)
    #print(q)
    r=q[::-1]
    for i in r:
        print(i,end="")
    
decimaltobinary(int(input()))
