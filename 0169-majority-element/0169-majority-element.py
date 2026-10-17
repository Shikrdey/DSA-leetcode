from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        l=max([i for i in d.values()])
        c=sum([i for i in d.values()])
        if l > c/2:
            for key, value in d.items():
                if value == l:
                    return key

        # d = Counter(nums)
        # m = max(d.values())
        # for k,val in d.items():
        #     if val == m:
        #         return k
