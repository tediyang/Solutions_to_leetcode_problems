class Solution:
    def mySqrt(self, x: int) -> int:
        sqr = x
        while not sqr * sqr - x < 1:
            sqr = ( sqr+ x / sqr) / 2
        return int(sqr)        