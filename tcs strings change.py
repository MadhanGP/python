s1=input()
s2=input()
s3=input()
for i in range(0,len(s1)):
    if s1[i]=='a' or s1[i]=='e' or s1[i]=='i' or s1[i]=='o' or s1[i]=='u' or s1[i]=='A' or s1[i]=='E' or s1[i]=='I' or s1[i]=='O' or s1[i]=='U':
        s1=s1.replace(s1[i],'"')
print(s1)

for i in range(0,len(s2)):
  if s2[i]=='a' or s2[i]=='e' or s2[i]=='i' or s2[i]=='o' or s2[i]=='u' or s2[i]=='A' or s2[i]=='E' or s2[i]=='I' or s2[i]=='O' or s2[i]=='U' :
    pass
  else:
    s2=s2.replace(s2[i],'*')
print(s2)

s4=s3.lower()
print(s4)
