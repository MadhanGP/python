from itertools import permutations
st=input()
d=permutations(st)
for i in list(d):
  print("".join(i))
