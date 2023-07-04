#----- print all the unrepeated char in the string (prob 2)------
# st=input("Enter the string:")
# oi=[]
# for i in st:
#     coun=st.count(i)
#     if coun<2:
#         oi.append(i)
# print("The Unrepeated Values are:",oi)

#------ remove the last vowel from the given string( prob 1)
# st=input("Enter the string:")
# strl=st[::-1]
# vowel=["a","i","o","e","u","A","E","I","O","U"]
# for i in range(len(st)):
#     if strl[i] in vowel:
#         new_st=strl.replace(strl[i],"-",1)
#         break
# print(new_st[::-1])

#----------- prob 3 (find out the longest palindromic substring from a given string)----
st=input("Enter the string:->")
s_s=[]
pali_sub=[]
for i in range(0,len(st)):
    for k in range(i+1,len(st)+1):
        s_s.append(st[i:k])
for j in s_s:
    if j==j[::-1]:
        pali_sub.append(j)
ul=0
mxpal=[]
for i in pali_sub:
    l=len(i)
    if l>ul:
        ul=l
for r in pali_sub:
    if len(r)==ul:
        mxpal.append(r)
print(mxpal)
# max_palsub=max(pali_sub,key=len)
# print(max_palsub)
