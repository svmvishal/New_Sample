from array import *

asc = array('i',[10,25,5,5,2,3,4,5])
asc = sorted(asc)
print(asc)


n = int(input("Enter the number"))
f = 1
for i in range(1,n+1):
    f= f *i
    i = i+1
print(f)

