import numpy

t=0
n=int(input())
aa=list(map(int,input().split()))

a=numpy.average(aa)
a=round(a)

for i in range(n):
  t+=(aa[i]-a)**2

print(int(t))