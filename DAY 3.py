# 1 Checking number is divisible by both 3 and 5
'''a=int(input("Enter a number:"))
if a%3==0 and a%5==0:
    print(f'{a} is divisible by both 3 and 5')
else:
    print(f'{a} is not divisible by both 3 and 5')'''

# 2 Checking the processing of ATM withdrawal
'''bal=int(input("Enter available balance:"))hi
amount=int(input("Enter withdrawal amount:"))
if bal>amount:
    print('ATM Withdrawal can be processed')
    bal-=amount
else:
    print('ATM Withdrawal cannot be processed')
print(f'Available balance : {bal}')'''

# 3 Checking student is seligible for admission
'''marks=int(input("Enter your marks:"))
cert=input("Do you have the sports quota certificate(yes/no):").lower()
if marks>=70 or cert=='yes':
    print('You are eligible for admission')
else:
    print('You are not eligible for admission')'''

# 4 Checking year is leap or not
year=int(input("Enter year:"))
if year%400==0 or year%4==0 and year%100==0:
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year') 