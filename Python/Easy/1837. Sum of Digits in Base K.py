class Solution:
    '''Solution to problem 1837'''
    def sumBase(self, n: int, k: int) -> int:
        '''Return the sum after being converted to the required base.'''
        result = 0
        # if the new value of n is less than the base, then exit loop and
        # add n to the result
        while n >= k:
            result += n % k # add the remainder
            n = n // k # divide n by the base and assign n to that value
        result += n 
        return result

# test cases
if __name__ == "__main__":
    case1 = Solution()
    print(case1.sumBase(34, 6))
    case2 = Solution()
    print(case2.sumBase(42, 2))
    case3 = Solution()
    print(case3.sumBase(10, 10))
