# this programme generates passes randomly that we can use them 
import string
import random
lenop=int(input("Enter the length of the password you want to generate:-"))
s1=string.ascii_lowercase
s2=string.ascii_uppercase
s3=string.punctuation
s4=string.digits
s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
random.shuffle(s)
print("The new pass for you: ")
print("".join(s[0:lenop]))