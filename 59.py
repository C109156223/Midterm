#59 硬幣及紙鈔的數量

money=int(input("輸入金額:"))

a1=money % 100
a2=a1 % 50
a3=a2 % 10
a4=a3 % 5

a=0
b=0


if money // 100 !=0:
    a=money // 100
    b=b+a
if a1 //50 !=0:
    a=a1 // 50
    b=b+a
if a2 // 10!=0:
    a=a2 // 10
    b=b+a
if a3 // 5 !=0:
    a=a3 // 5
    b=b+a
if a4 // 1 !=0:
    a=a4 // 1
    b=b+a
print(b)
    
    
    
    
    
    
    
    
    
    
    
    
    
    