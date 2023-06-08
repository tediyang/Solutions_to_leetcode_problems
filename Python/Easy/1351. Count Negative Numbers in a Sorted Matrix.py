class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        count = 0
        for row in grid:
            for col in row:
                if col < 0:
                    count += 1
        return count