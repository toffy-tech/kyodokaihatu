a=int(input("A="))
b=int(input("B="))
c=int(input("C="))
t=int(input("T="))
x=0

for i in range(a+1):
  for j in range(b+1):
    for k in range(c+1):
      if t==i*500+j*100+k*50:
        x+=1

print(str(x)+"回")