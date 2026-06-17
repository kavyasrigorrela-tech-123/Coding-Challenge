# 1 Sum of first N natural numbers
n=int(input("Enter a number : "))
sum=0
for i in range(1,n+1):
    sum+=i
print(f'Sum of first {n} numbers is {sum}')

# 2 Printing multiplication table of a number from 1 to 10
n=int(input("Enter a number : "))
for i in range(1,11):
    print(f'{i}*{n}={i*n}')

# 3 Count digits in a number
n=int(input("Enter a number : "))
N=n
c=0
while n>0:
    c+=1
    n=n//10
print(f'The number of digits in {N} is {c}')

# 4 Reversing a number
n=int(input("Enter a number : "))
res=0
while n>0:
    r=n%10
    res=res*10+r
    n//=10
print(f'Reversed number is {res}')

# 5 Check given number is  prime or not
n=int(input("Enter a number : "))
flag=0
for i in range(2,int(n**0.5) + 1):
    if n%i==0:
        flag=1
        break
if flag==0:
    print(f'{n} is prime number')
else:
    print(f'{n} is not prime number')