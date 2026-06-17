# 1 Print the index of largest element in list of integers
l=[2000,15,78,63,320]
large=max(l)
ind=l.index(large)
print(f"Index of largest element i.e.{large} in list i.e.{l} is {ind}")

# 2 Counting largest element appearance in given list of integers
l=[1,3,40,23,40,3,55,60,55,55,60]
large=max(l)
c=l.count(large)
print(f'Count of largest element i.e.{large} in list i.e.{l} is {c}')

# 3 Checking the given list is sorted or not in asc order
l=[1,29,2,7,8]
s=sorted(l)
if(l==s):
    print(f'Given list i.e.{l} is sorted in ascending order')
else:
    print(f'Given list i.e.{l} is not sorted in ascending order')

# 4 Given a list & key ,Checking if key exist in list
l=[20,30,45,78,64]
key=78
if key in l:
    print(f'{key} exist in {l}')
else:
    print(f'{key} does not exist in {l}')

# 5 Printing diff between sum of even and sum of odd numbers in given list
l=[1,2,3,4,5,6,7,8]
el,ol=[],[]
for i in l:
    if i%2==0:
        el.append(i)
    else:
        ol.append(i)
esum,osum=sum(el),sum(ol)
diff=esum-osum
print(f'Diff between sum of even & sum of odd numbers in list i.e.{l} is {diff}')

# 6 Removing all occurances of element from given array
l=[24,64,46,32,78,46,32,46]
n=int(input(f"Enter a number you want to remove from the list {l} :"))
if n not in l:
    print(f'{n} is not present in {l} so no removal is done')
for i in l:
    if i==n:
        l.remove(n)
print(l)

# 7 Printing a new list containing double of each element in given list
l=[10,40,50,60]
r=[]
for i in l:
    r.append(i*2)
print(r)