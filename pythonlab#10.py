#--------- problem 1----
# lis=[]
# st=input("Enter the string: ")
# for i in st:
#     if i not in lis:
#         x=st.count(i)
#         lis.append(i)
#         print(i,"is located",x,"times")
#     print()
# -------- problem 2 -------
# ra=int(input("Enter number:"))
# fac=[]
# def fact(x):
#     for i in range(1,x+1):
#         if x%i==0:
#             fac.append(i)           
# fact(ra)
# print(fac)
# odd=[]
# for i in fac:
#     if i%2!=0:
#         odd.append(i)
# print("The odd factors are:",odd)
# res=sum(odd)
# print("The sum of odd numbers :",res)
# ------- problem 3-------
# ra=int(input("Enter number:"))
# fac=[]
# def fact(x):
#     for i in range(1,x+1):
#         if x%i==0:
#             fac.append(i)   
# pn=[]            
# print("The prime factors are")       
# j=1
# while(j<=ra):
#     k=0
#     if(ra%j==0):
#         n=1
#         while(n<=j):
#             if(j%n==0):
#                 k=k+1
#             n+=1
#         if(k==2):
#             pn.append(j)
#     j+=1
# print(pn)
# mul=1
# for m in pn:
#     mul*=m
# print("The product of the odd numbers is:->",mul)
#------problem 4 -------
nu=int(input("Enter number:"))
fac=[]
def fact(x):
    for i in range(1,x+1):
        if x%i==0:
            fac.append(i)          
fact(nu)
print("The factorials of this numbers are:",fac)
max=max(fac)**2
