import math
n=int(input("Enter the number"))
array=[]

for i in range(1,math.isqrt(n)+1):

    if(n%i==0):
        array.append(i)
        if(i!=n//i):
            array.append(n//i)


array.sort()

print(array)
