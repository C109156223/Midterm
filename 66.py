#66

x=set(input("請輸入string_a:"))
y=set(input("請輸入string_b:"))

z=x&y
zz=sorted(z)
zzz="".join(zz)
print(zzz)