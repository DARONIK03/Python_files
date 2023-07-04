#  -----------  problem 3 --------
# st=input("Enter the string:")
# lis=st.split(" ")
# print("The inputed string is:",st)
# print("The even words in the list is:")
# for i in lis:
#     if len(i):
#         if len(i)%2==0:
#             print(i)
#  -----------  problem 2 --------
# ing=int(input("Enter the number of words: "))
# string=[]
# x=0
# c=0
# for i in range(ing):
#     string.append(input("Enter  words:"))
# print("The inputed strings are:")
# print(string)
# for j in string:
#     if len(j)>x:
#         x=len(j)
#         c=j
# print("The biggest string in this list is :",c)
#---------------- problem 4 ------
# st=input("Enter the string:")
# print("The inputed string is:",st)
# pos=int(input("Enter the position of the charecter should be deleted:"))
# def del_char(string,position):
#     a=string[:position]
#     b=string[position+1:]
#     return a+b
# print("The rectified string is:",del_char(st,pos))
# ---------------problem 5 -------
# st=[]
# k=0
# print("Enter the number of strings: ")
# num=int(input("->"))
# for i in range(num):
#     st.append(int(input("Enter number ->")))
# print("The inputed numbers are :",st)   
# leng=int(input("Enter the limit: "))
# for i in st:
#     if i>leng:
#         k+=1
# print("There are",k,"numbers in this list,greater than the limit")
#-------------- problem 1 --
lis=[]
print("Enter the length of array: ")
num=int(input("->"))
for i in range(num):
    lis.append(int(input("Enter number ->")))
print("The inputed numbers are :",lis) 
def final_lis(n) :
    pos=3-1 
    flag=0 
    ln=len(n)  
    while ln>2:
        flag=(pos+flag)%ln
        print(n.pop(flag))
        ln-=1
final_lis(lis)