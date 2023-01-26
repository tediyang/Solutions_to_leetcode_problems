import random

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        fac = lambda x: 1 if x <= 1 else x * fac(x-1)

        n = len(nums)
        per_v = int(fac(n)/ fac(n-n))

        new_ans = []

        while len(new_ans) != per_v:
            shf = random.sample(nums, len(nums))
            if shf not in new_ans:
                new_ans.append(shf)

        return  new_ans
