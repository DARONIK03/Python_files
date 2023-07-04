# WAP to print the current date and time
from email.utils import localtime
import time 
T=time.localtime(time.time())
localtime=time.asctime(T)
str="current time of thr place:"+ time.asctime(T)
print(str)


