class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        l=[]
        a=len(nums)
        for i in range(a):
            b=target-nums[i]
            
            if b in nums and i!=nums.index(b):
                l.append(i)
                l.append(nums.index(b))
                return(l)