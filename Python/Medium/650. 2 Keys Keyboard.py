class Solution:
    def minSteps(self, n: int) -> int:
        count = 0 
        div = 2
        temp = n
        
        if n == 1:
          return 0
        
        while div < n and temp > 1:
            if temp % div != 0:
                div += 1
            else:
                count += div
                temp //= div

        if count == 0:
            return n
        
        return count 
        