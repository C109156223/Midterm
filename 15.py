#15 數字加密

n=input("輸入一組四位數字為:")

n1=[]
n2=[]

n1=list(n)

for i in range(len(n1)):
    n2.append((int(n1[i])+7)%10)
    
ans=str(n2[2])+str(n2[3])+str(n2[0])+str(n2[1])
print(ans)
