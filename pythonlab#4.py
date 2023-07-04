# a=int(input("Enter first number:-"))
# b=int(input("Enter second number:-"))
# c=int(input("Enter third number:-"))
# if a>b :
#     if a>c :
#         print("the first number is greatest")
#     else:
#         print("The third number is greatest")
# else :
#     if b>c :
#         print("The second number is the greatest")
#     else :
#         print("The third number is the greatest")
#======================================================

# a=ord(input("Enter the charecter:-"))
# if (a>=65 and a<=90) :
#     print("The Charecter is a Uppercase letter")
# elif (a>=97 and a<=122) :
#     print("The Charecter is a Lowercase letter")
# else :
#     print("This is not a charecter")
#======================================================
# whl=input("Enter your message:-")
# num=int(input("Enter the number of times you want to print:-"))
# while num>0 :
#         print(whl)
#         num=num-1
#======================================================

# var1=int(input("Enter the number :- "))
# i=1
# fac=1
# while i <= var1 :
#         fac=fac*i
#         i=i+1
# print("The factorial value of the number is :- ",fac)

#======================================================
varn=int(input("Enter the number:- "))
r=0
while varn>0 :
        r=(r*10) + varn % 10
        varn=varn//10
print("reverse of the entered number is:-",r)
