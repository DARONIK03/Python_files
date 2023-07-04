# (develop a dictionary by using python) made your own dictionary by python 0
 
# dic ={"python":"the most advance programming language","java":"the most used pro.. lang in india","ruby":" the only ios language","C":" the most basic and complecated old language"}
# i =input("enter the programming language you want to know about:--\n")
# o =i.capitalize()
# print(o,"=",dic[i])

# Develop a faulty calculator with this following faults: 45*3 = 555 , 56+9 = 77 ,56/6 = 4
oper = input ('''please enter the operation you want you to do:
            enter '+'for add 
            enter '-'for substraction 
            enter '*'for multiplication
            enter '/'for divide 
            enter '**'for power 
            enter '%'for modulus
            please enter your choice :- ''' )

print("enter the first number N1:")
N1 = int(input())
print("enter the 2nd number N2:-")
N2 = int(input())
if oper == '+' :
    resu = N1 + N2 
    if N1 == 56 and N2 == 9 :
        resu = 77
elif oper == '*' :
    resu = N1 * N2
    if N1 == 45 and N2 == 3 :
        resu = 555
elif oper == '/':
    resu = N1/N2
    if N1 == 56 and N2 == 6 :
        resu = 4 
else :
    resu = N1 - N2

print("result =",resu)
print("address of N1 in integer form is: ",int(id(N1)));

