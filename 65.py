#65

x=set(input("請輸入A的好友:").split(" "))
y=set(input("請輸入B的好友:").split(" "))
z=x&y
print(len(z))