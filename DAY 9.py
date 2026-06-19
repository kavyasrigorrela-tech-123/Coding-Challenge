# 1 Checking given number is prime or not
import math
n=int(input("Enter a number : "))
if n<=1:
    print("Not prime")
else:
    flag=0
    for i in range(2,n//2):
        if n%i==0:
            flag=1
            break
    if(flag==1):
        print(f'{n} is not prime')
    else:
        print(f'{n} is prime')