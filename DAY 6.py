# 1 Printing elements of the array
arr=[10,20,30,40,50]
for i in range(0,len(arr)):
    print(arr[i])

# 2 Printing sum of elements of given array
arr=[10,20,30,40,50]
sum=0
for i in arr:
    sum+=i
print(f'Sum of elements in {arr} is {sum}')

# 3 Printing the largest element in the array
arr=[10,-200,30,40,50]
large=arr[0]
for i in range(1,len(arr)):
    if arr[i]>large:
        large=arr[i]
print(f'Largest element in {arr} is {large}')

# 4 Printing the smallest element in the array
arr=[10,200,30,40,50]
small=arr[0]
for i in range(1,len(arr)):
    if arr[i]<small:
        small=arr[i]
print(f'Smallest element in {arr} is {small}')

# 5 Counting even numbers present in given array
arr=[10,-203,3,45,50]
count=0
for i in arr:
    if i%2==0:
        count+=1
print(f'No. of even numbers in {arr} is {count}')

# 6 Printing odd numbers in given array
arr=[10,20,45,33,70,85]
print(f'Odd numbers in {arr} :')
for i in arr:
    if i%2!=0:
        print(i)

# 7 Counting numbers that are greater than 10 in given array
arr=[10,-203,65,45,50]
count=0
for i in arr:
    if i>10:
        count+=1
print(f'There are {count} numbers that are greater than 10 in {arr}')
# 8 Printing a new array containing sqares of elements in given array
arr=[11,2,3,8,10]
res=[]
for i in arr:
    res.append(i*i)
print(res)

# 9 Printing elements in reverse order
arr=[1,2,3,4,5]
print(f'Printing elements in {arr} in reverse order:')
for i in range(len(arr)-1,-1,-1):
    print(arr[i],end=' ')

# 10 Printing avg of elements in given array
arr=[10,20,20,25,20]
sum=0
for i in arr:
    sum+=i
avg=sum/len(arr)
print(f'Avg of elements in {arr} is {avg}')