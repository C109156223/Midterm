#52

x=int(input("輸入n值:"))
dict1={}

for i in range(0,x):
    y=input("請輸入姓名:")
    z=input("請輸入電子郵件:")
    dict1[y]=z
    
q=input("請輸入要查詢電子郵件的姓名:")

if q in dict1:
    print(q+"電子郵件帳號為"+dict1[q])
    
    