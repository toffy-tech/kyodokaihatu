a=[]

while True:
  e=input("数字を入力してください:")
  if e=="":
    break
  else:
    a.append(e)

a=set(a)

print(len(a))