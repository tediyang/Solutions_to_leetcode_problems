class Solution:
    def romanToInt(self, s: str) -> int:
        
        new_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        r_list, number = [], 0
        
        
        for r in s:
            if not number:
                r_list.append(r)
                number += new_dict[r]
                
            else:
                if (r_list[-1] == 'I' and (r == 'V' or r == 'X')) or (r_list[-1] == 'X' and 
                    (r == 'L' or r == 'C')) or (r_list[-1] == 'C' and (r == 'D' or r == 'M')):
                    number += (new_dict[r] - new_dict[r_list[-1]]*2)
                    
                else:
                    r_list.append(r)
                    number += new_dict[r]
                
        return number
                
