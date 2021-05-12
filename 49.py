#49 找出班上成績問題

a=set(["John","Mary","Tina","Fiona","Claire","Eva","Ben","Bill","Bert"])
eng=set(["John","Mary","Fiona","Claire","Ben","Bill"])
mat=set(["Mary","Fiona","Claire","Eva","Ben"])
print("英文與數學都及格",eng & mat)
print("數學不及格",a-mat)
print("英文及格且數學不及格",eng& a-mat)