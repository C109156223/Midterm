#62 水果 顏色

x=input("請輸入水果:")
dict1={"蘋果":"紅色","香蕉":"黃色","葡萄":"紫色","藍莓":"藍色","橘子":"橘色"}
if (x in dict1):
    print(x+"是"+dict1[x])
else:
    y=input("請輸入顏色:")
    dict1[x]=y
    print(x+"是"+dict1[x])