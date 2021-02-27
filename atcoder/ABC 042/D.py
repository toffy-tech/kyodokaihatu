h,w,a,b=map(int,input().split())

aa = [[0 for _ in range(w)] for _ in range(h)]

for i in range(h):
  for j in range(w):
    if i>=h-a and j<b:
      pass
    else:
      if i==0 or j==0:
        aa[i][j]=1
      else:
        aa[i][j]=aa[i-1][j]+aa[i][j-1]

print(str(aa[h-1][w-1]))