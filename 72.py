#72

x=int(input("請輸入n："))
y=int(input("請輸入k："))

z=x//y  #菸屁股可以換成幾支菸


if (z>y):
    ans=x+z
    while(z>=y):
        z=z//y
        ans=ans+z
elif(z<y):
    ans=x+z

print("Peter可以抽"+str(ans)+"支紙菸")



    