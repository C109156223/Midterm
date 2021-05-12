#3 生肖 西元4年=鼠 2008=鼠

x=int(input("請輸入西元年:"))
list1=["rat","ox","tiger","rat","dragon","snake","horse","sheep","monkey","rooster","dog","pig"]
if (x>4):
    print(list1[(x-4)%12])
else:
    print(list1[x])