# -------------  Transpose matrix --------------------
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
# print("The transpose matrix of the inputed matrix will be:")
# for i in range (R):
#     for j in range (C):
#         print("\t",matrix[j][i],end="")
#     print()
#--------------- kth column --------------------
# mat=[[1,3,43,45],[96,293,7,87]]
# print("The taken matrix is:"+str(mat))
# k=int(input("Enter the column number:"))
# final_mat=[sub k for sub in mat]
# print(+str(final_mat))
#------------- problem 3 ---------------
# st=input("Enter string: ")
# fq={}
# for i in st:
#     if i in fq:
#         fq[i]=fq[i]+1
#     else:
#         fq[i]=1
# final=min(fq,key=fq.get)
# print(final)
# ---------------------problem 5 ------
# n=int(input("Enter the number:"))
# dec=0
# for i in str(n):
#     if int(i)!=0 and n%int(i)==0:
#         dec=1
#     else:
#         dec=0
# if dec==1:
#     print("The number is devisible by its digits")
# else:
#     print("no! The number is not divisible by its digits")
#------------------problem 6 -----------
# k=int(input("Enter digit:"))
# n=int(input("Enter diviser:"))
# def fun(k,n):
#     vl=pow(k,n)
#     if(vl%n==0):
#         return vl
#     else:
#         return((vl+k)-((vl+k)%k))
# print(fun(k,n))
# --------------------- pattern prob 4 --------------
rng=int(input("Enter the number of rows needed for the pattern:"))
k=1
for i in range(0,rng):
    for s in range(i,rng):
        print(" ",end=" ")
    for a in range(i):
        if i%2!=0 and a%2==0:
            print("&",end=" ")
        elif i%2==0 and a%2!=0:
            print("&",end=" ")
        else:
            print(" ",end=" ")
    for k in range(i+1):
        if k%2==0:
            print("&",end=" ")
        else :
            print(" ",end=" ")
    print("")