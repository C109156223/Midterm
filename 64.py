#64 孿生質數

x=int(input("請輸入第一個要判斷的數字:"))
y=int(input("請輸入第二個要判斷的數字:"))
a=x % 2
b=y % 2

if (a==0 or b==0):
    print("N")
else:
    print("Y")