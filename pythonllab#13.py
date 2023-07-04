#-------- find the missing positive numbers of a given list 
# a=[]
# mis=[]
# n=int(input("Enter number of elements:"))
# for i in range(n):
#     a.append(int(input("Enter value:")))
# print("The taken array is :",a)
# max=max(a)
# sor=[]
# for i in range(len(a)):
#     if i>0:
#         sor.append(i)
# min=min(sor)
# print("The maximum and minimum number of the list as respected:",max,min)
# for i in range(min,max+1):
#     if i not in a:
#         mis.append(i)
# print("The missing numbers in the list are:",mis)

# ------  find out the biggest difference between the two sucessor elements in the given list -----
# lis=[]
# n=int(input("Enter no. of elements in the list:"))
# for i in range(n):
#     lis.append(int(input("ent val:")))
# print("Taken list:",lis)
# ma=[]
# for j in range(1,len(lis)):
#     ma.append(lis[j]-lis[j-1])
# print("The maximum difference between two adjecent numbers in the list is:",max(ma))

# ------  fetch a window string including the charecters entered by user from the given string -----
# code @ geeks for geeks
# no_of_chars = 256

# def findSubString(string, pat):

# 	len1 = len(string)
# 	len2 = len(pat)

	
# 	if len1 < len2:

# 		print("No such window exists")
# 		return ""

# 	hash_pat = [0] * no_of_chars
# 	hash_str = [0] * no_of_chars

	
# 	for i in range(0, len2):
# 		hash_pat[ord(pat[i])] += 1

# 	start, start_index, min_len = 0, -1, float('inf')

	
# 	count = 0 
# 	for j in range(0, len1):

		
# 		hash_str[ord(string[j])] += 1

		
# 		if (hash_str[ord(string[j])] <=
# 				hash_pat[ord(string[j])]):
# 			count += 1


# 		if count == len2:

			
# 			while (hash_str[ord(string[start])] >
# 				hash_pat[ord(string[start])] or
# 				hash_pat[ord(string[start])] == 0):

# 				if (hash_str[ord(string[start])] >
# 						hash_pat[ord(string[start])]):
# 					hash_str[ord(string[start])] -= 1
# 				start += 1

			
# 			len_window = j - start + 1
# 			if min_len > len_window:

# 				min_len = len_window
# 				start_index = start

# 	if start_index == -1:
# 		print("No such window exists")
# 		return ""

	
# 	return string[start_index: start_index + min_len]


# if __name__ == "__main__":

# 	string =input("Enter a strin for s:")
# 	pat = (input("Enter  a string for t:"))

# 	print(findSubString(string,pat))
# =====                  OR               ==------
st=input("Enter the string:")
st2=input("Enter the 2nd string:")
substring=[]
sor=[]
yes=0
if len(st)<len(st2):
    print("No window found as big as that")
elif len(st)==len(st2):
    for i in st2:
        if  i in st:
            yes=1
    if yes==1:
        print(st)
else :
    for i in range(0,len(st)):
        for k in range(i+1,len(st)+1):
            substring.append(st[i:k])
    for j in substring:
        for k in st2:
          if k in j:
              yes=1
        if yes==1:
            sor.append(j)
    sup=max(sor,key=len)
    print(sup)
        
    
