#          MATRIX WITH THE HELP OF PYTHON 
#
# R=int(input("Enter the number of rows:-"))
# C=int(input("Enter the number of columns:- "))
# matrix=[]
# for i in range(R):
#     mat=[]
#     for j in range(C):
#         mat.append(int(input("Elements:")))
#     matrix.append(mat)
# print("The inputed matrix is : ")
# for i in range (R):
#     for j in range (C):
#         print("\t",matrix[i][j],end="")
#     print()
#==========   operations with matrix 
#
matrix=[]
matrix2=[]
final_mat=[]
print("Enter the first matrix : ")
R=int(input("Enter the number of rows:-"))
C=int(input("Enter the number of columns:- "))
for i in range(R):
    mat=[]
    for j in range(C):
        mat.append(int(input("Elements:")))
    matrix.append(mat)
for i in range (R):
    for j in range (C):
        print("\t",matrix[i][j],end="")
    print()
print("Enter the 2nd matrix:")
R=int(input("Enter the number of rows:-"))
C=int(input("Enter the number of columns:- "))
for i in range(R):
    mat2=[]
    for j in range (C):
        mat2.append(int(input("Element: ")))
    matrix2.append(mat2)
for i in range (R):
    for j in range (C):
        print("\t",matrix2[i][j],end="")
    print()

print("Matrix addition : ")
for i in range (R):
    add=[] 
    for j in range (C):
        add.append(matrix[i][j]+ matrix2[i][j])
    final_mat.append(add)
print("After add the matrix is: ")
for i in range (R):
    for j in range (C):
        print("\t",final_mat[i][j],end="")
    print("")

print("Matrix multiplication: ")
for i in range (R):
    for j in range (C):
        for k in range (C):
            final_mat[i][j]+=matrix[i][j]*matrix2[j][i]
for R in final_mat:
    print(R) 
#=============         ==  Problem 1==================
# pr=[]
# for i in range(0,21):
#     if i%2==0 or i%4==0 :
#         pr.append(i)
# print("The final list is :",pr,end="")   
#=========     ============== problem 2     ===============
# lis=[] 
# sum=0
# for i in range(1,11):
#     lis.append(i)
# print("The list is :",lis)
# for k in range(1,11):
#     sum=sum+(k*k)
# print("The sum of the squared list: ",sum)
#==========          =============  problem 3    ========
# evnlis=[]
# for i in range(0,11):
#     evnlis.append(i)
# print("The current list is",evnlis)
# sortlis=list(filter(lambda m:(m%2!=0),evnlis))
# print("The sorted list is: ",sortlis)
#=======          ==================     problem 4           ==========
# lis=[12,48,79,76,48]
# pos=[]
# item=int(input("Enter the item you want to search: "))

# for i in range(len(lis)):
#     if lis[i]==item:
#         pos.append(i)
# print("The positions where the inputed element exists is : ",pos)
#=========================      problem dd-mm-yyyy                  ===============
# a=[]
# n=int(input("Enter the number of dates: "))
# for i in range(0,n):
#     date=input("Enter date: ")
#     a.append(date.split("/"))
# print("The seperated dates are:")
# #print(a)
# #new_l = [i for b in map(lambda x:[x] if not isinstance(x, list) else x, a) for i in b]
# newl=sum(a,[])
# #print(new_l)
# print("The inputed dates are:")
# print(newl[::3])
# print("The inputed months are:")
# print(newl[1::3])
# print("The inputed years are:")
# print(newl[2::3])