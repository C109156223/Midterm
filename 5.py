#5 階層判斷

m=int(input("請輸入階層值M:"))
total=i=1
while (total<=m):
    total=total*i
    i=i+1
print("超過M為"+str(m)+"的最小階層N值為:"+str(i-1))