# inp=input("enter the string:- ")

# for i in inp:
#     if i==3:
#         continue;
#     elif i==6:
#         break;
#     else:
#         print(i)
#     print("")
# print("this is the end")
#======================================
# speak=input("Enter the string:- ")
# length=len(speak)
# p=0
# for k in range(-1,(-length-1),-1):
#     print(speak[p],"\n\t",speak[k])
#     p=p+1
#=====================================
# string=input("Enter the string:- ")
# rev=string[::-1]
# if string==rev :
#     print("palindrome")
# else:
#     print("not palindrome")
#=====================================
# aln=input("Enter the string:- ")
# if aln.isalpha:
#     print("The string atleast have a number or an symbio")
# else:
#     print("this is not a alphanumeric string")
#====================================
# cap=input("Enter The string: ")
# out=(cap.capitalize())
# print("the capitalize form is: ",out)
#====================================
# freq=(input("enter the number:"))
# c=0
# for k in freq:
#     if freq.isdigit():
#         c=c+1
# print("the frequency of the number is:",str(c))
#====================================
def app(a,b):
    c=a+b
    print("the addition of two numbers:")
    return c
inpa=int(input("Enter the first value:- "))
inpb=int(input("Enter the second value:- "))
print(app(inpa,inpb))