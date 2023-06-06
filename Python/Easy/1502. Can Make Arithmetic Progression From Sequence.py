class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        sort_list, lnth = sorted(arr), len(arr)

        i, j = 0, 2
        while(j < lnth):
            if abs(sort_list[i+1] - sort_list[i]) != sort_list[j] - sort_list[i+1]:
                return False
            i += 1
            j += 1
        return True