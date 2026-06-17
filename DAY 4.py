# 1 Printing numbers from 1 to 1000
'''for i in range(1,1001):
    print(i)'''

# 2 Printing multiplication table of a number
'''n=int(input("Enter a number : "))
for i in range(1,11):
    print(f'{i}*{n}={i*n}')'''

# 3 Printing even numbers from one to n
'''n=int(input("Enter a number : "))
print(f"Even numbers between 1 and {n}")
for i in range(1,n+1):
    if i%2==0:
        print(i)'''

# 4 Printing odd numbers from one to n
'''n=int(input("Enter a number : "))
print(f"Odd numbers between 1 and {n}")
for i in range(1,n+1):
    if i%2!=0:
        print(i)'''

# 5 Calculating factorial of a given number
n=int(input("Enter a number : "))
fact=1
for i in range(1,n+1):
    fact*=i
print(f'Factorial of {n} is {fact}')