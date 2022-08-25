class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, n in enumerate(nums):
            if target == n:
                return i
            
            elif target < n and i == 0:
                return i
            
            elif target < n:
                return i-1
            
            elif len(nums) -1 != i:
                if n < target < nums[i+1]:
                    return i+1
                
            else:
                return i+1
                    
                
          
                            
        