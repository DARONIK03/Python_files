#-------- remove the ith occurrence in a list (for int only)----
# n=int(input("Enter the number of elements in the list:"))
# lis=[]
# for i in range(n):
#     lis.append((input("Enter element:")))
# print("The inputed list is:",lis)
# pos=int(input("Enter the position of removal: "))
# for j in lis:
#     if lis[pos]==j:
#         print("The item is occering multiple time in the list")
#         print("The removed list is:")
#         lis.pop(pos-1)
#     else :
#       print("The item dosen't exists multipletimes in the list so deletion does not needed!!")
# print(lis)

#------------- problem 2 ----------
# n=int(input("Enter the number of elements in the list:"))
# lis=[]
# for i in range(n):
#     lis.append(int(input("Enter element:")))

# def findLargest(arr):
# 	secondLargest = 0
# 	largest = min(arr)

# 	for i in range(len(arr)):
# 		if arr[i] > largest:
# 			secondLargest = largest
# 			largest = arr[i]
# 		else:
# 			secondLargest = max(secondLargest, arr[i])

# 	# Returning second largest element
# 	return secondLargest

# # Calling above method over this array set
# print("The 2nd largest element is: ",findLargest(lis))


#-------- pattern (prob 4--
# r=int(input("Enter the number of rows:"))
# for i in range(r):
#     for s in range(1,(r-i)*2-1):
#         print(" ",end=" ")
#     for k in range(1,i*2):
#         print("*",end=" ")
#     print()

# ----------- pattern(prob 3)(ladder pattern) ---
# r=int(input("Enter the number of the rows: "))
# for i in range(1,r+1):
#     for j in range(i*2-1):
#         print("*",end=" ")
#     print()
# ------------- problem 5 (Bubble sort)-----------------
# arr=[]
# n=int(input("Enter the No of elements you want to input:"))
# for i in range(n):
#     arr.append(int(input("Enter value:")))
# print("The entered lis is:",arr)

# def bubble(lis):
#     listlength=len(arr)-1
#     sorted=False

#     while not sorted:
#         sorted=True
#         for i in range(0,listlength):
#             if arr[i]>arr[i+1]:
#                 sorted=False
#                 arr[i],arr[i+1]=arr[i+1],arr[i]
#     return arr
# print("The sorted list is :",bubble(arr))

# ------------ count occurrence of a word in a string ------
st=input("Enter the string:")
p=st.split(" ")
spare_lis=[]
length=len(p)
i=0
while i<length:
    count=0
    for j in p:
        if p[i]==j:
            count+=1
            spare_lis.append(p[i])
    print(p[i],"\t has occurred ->",count,"times")
    i+=1
