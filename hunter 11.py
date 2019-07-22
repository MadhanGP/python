string=map(str,input().split())
rev=[i[::-1] for i in string]
for j in rev:
  print(j,end=" ")
