# def area_rec(a,b):
#     c=a*b
#     print("The area of the rectangle is:-")
#     return c
# inp=int(input("Enter the length:- "))
# inp2=int(input("Enter the width:- "))
# print(area_rec(inp,inp2))
#===============================
# def appe(lis):
#     lis=[12,13,14]
#     print(lis)
# list=[1,12,33,4,78]
# appe(list)
# print(list)
#===============================
# def function_me(arg,*vartouple):
#     print("arg output:- ")
#     print(arg)
#     print("var output:- ")
#     for var in vartouple:
        
#         print(var)
#     return ;
# function_me(34,44,78,89)
#===============================
# multyiply=lambda i:i**2
# number=int(input("Enter the Number: "))
# print("The square of the inputed number is :- ",multyiply(number))
#===============================
# ank_list=[28,34,64,21,81]
# filt_lis=list(filter(lambda m:(m%2==0 & m%7==0),ank_list))
# print("The new filtered list is :",filt_lis)
# ================================
# def farhenheit(T):
#     return((float(9)/5)*T+32)
# def celsius(T):
#     return((float(5)/9)*(T-32))
# tempereture=[37,46,79,23,87]
# F=list(map(farhenheit,temperetur))
# C=list(map(celsius,F))
# print(F)
# print(C)
#=================================
#factorial by funct 
# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# a=int(input("Enter the number:- "))
# print(factorial(a))
#=================================
# lis=[11,26,33,40]
# lis2=[7,90,88,120]
# print("Original list:")
# print(lis)
# print(lis2)
# final_list=list(map(lambda a,b:(a+b),lis,lis2))
# print("The final list is :",final_list)
#===================================
lis_days=["Monday",'Tuesday','ecoday','wednesday','thursday','friday','sunday','funday']
sort_list=filter(lambda day:day if len(day)==6 else '',lis_days)
for s in sort_list:
    print(s)