from functools import reduce

class Solution:
    def fractionAddition(self, expression: str) -> str:
        state = ""
        denom = []
        numer = []
    
        for i in expression:
          if i == '-':
            if state:
              denom.append(int(state))
            state = i
          
          elif i == '+':
            if state:
              denom.append(int(state))
            state = i
            
          elif i == '/':
            if state:
              numer.append(int(state))
            state = ""
          
          else:
            state += i

        # Add the last denominator
        denom.append(int(state))

        total_denom = reduce(lambda x, y: x * y, denom)
        total_numer = sum([i * (total_denom / j) for i, j in zip(numer, denom)])
        if total_numer == 0:
            return "0/1"
        
        return self.breakdown(total_numer, total_denom)

    def breakdown(self, num, dem):
        i = 2
        while i <= dem:
            if num % i == 0 and dem % i == 0:
                num /= i
                dem /= i
            else:
              i += 1

            if num == 1:
                break

        return f"{int(num)}/{int(dem)}"
