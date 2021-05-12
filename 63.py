#63 Perfect Number

data1=0
n=int(input("請輸入正整數n:"))
for i in range(1,n):
    if n % i ==0:
        data1=data1+i
if data1 == n :
    print("perfect")
elif data1 > n :
    print("abundant")
elif data1 < n:
    print("deficient")