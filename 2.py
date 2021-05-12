#2 計算電費 區間計算

x=int(input("輸入一個度數(正整數)"))
if (x<121):
    print("Summer months:",x*2.10)
    print("Non-Summer months",x*2.10)
elif (x<331 and x>120):
    print("Summer months:",120*2.10+(x-120)*3.02)
    print("Non-Summer months",x*2.10+(x-120)*2.68)
elif (x<501 and x>330):
    print("Summer months:",120*2.10+210*3.02+(x-330)*4.39)
    print("Non-Summer months",120*2.10+210*2.68+(x-330)*3.61)
elif (x<701 and x>500):
    print("Summer months:",120*2.10+210*3.02+170*4.39+(x-500)*4.97)
    print("Non-Summer months",120*2.10+210*2.68+170*3.61+(x-500)*4.01)
elif (x>700):
    print("Summer months:",120*2.10+210*3.02+170*4.39+200*4.97+(x-700)*5.63)
    print("Non-Summer months",120*2.10+210*2.68+170*3.61+200*4.01+(x-700)*4.50)