a,b=list(map(int,input().split()))
c,d=list(map(int,input().split()))
e,f=list(map(int,input().split()))
if a==b or c==d or e==f or a==c==e or b==d==f:
    print('yes')
else:
    print('no')
