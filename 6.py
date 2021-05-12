#6 兩數差值

a=input("請輸入值為:").split(",")
a.sort()
b=list(reversed(a))

x1=""
x2=""

for i in range(len(a)):
    x1=x1+a[i]
    x2=x2+b[i]
b=int(x2)-int(x1)

print(str(b))


