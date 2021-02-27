aa=list(map(int,input().split()))
t=0

if aa[0]+aa[1]+aa[2]==17:
  for i in range(3):
    if aa[i]==5:
      t+=1

if t==2:
  print("Yes")
else:
  print("No")