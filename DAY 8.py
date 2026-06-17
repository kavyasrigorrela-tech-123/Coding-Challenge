# LEETCODE PROBLEMS

# 1 Neither minimum nor maximum(2733)
'''class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        n=len(nums)
        if(n<=2):
            return -1
        else:
            nums.sort()
            return nums[1]'''

# 2 Missing number(268)
'''class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(0,n+1):
            if i not in nums:
                return i'''

# 3 Find the duplicate number(287)
'''class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l=set()
        for i in nums:
            if i in l:
                return i
            l.add(i)'''

# 4 Find numbers with even number of digits(1295)
'''class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            if len(str(i))%2==0:
                count+=1
        return count'''
