a=[]
c=0


for i in range(200):
    j=input()
    if j=="q" or j=="":
        break
    j=int(j)
    a.append(j)

while True:
    b=0
    for i in range(len(a)):
        if a[i]%2==1:
            b=1
            break
    if b==1:
        break
    for i in range(len(a)):
        a[i]=a[i]/2
    c+=1


print(a)
print(c)