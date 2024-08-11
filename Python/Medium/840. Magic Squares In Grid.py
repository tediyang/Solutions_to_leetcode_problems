from typing import List


class Solution:
  def __init__(self):
      self.ans = 0

  def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
    if len(grid) < 3 or len(grid[0]) < 3:
      return self.ans

    rows = len(grid[0])
    cols = len(grid)

    for i in range(cols - 2):
      new_grid = grid[0 + i: 3 + i]

      for j in range(rows - 2):
        sub_grid = []
        for data in new_grid:
          sub_grid.append(data[0 + j: 3 + j])
        self.verify_magic_square(sub_grid)

    return self.ans

  def verify_magic_square(self, sub_grid: List[List[int]]) -> None:
    result = [sum(data) for data in sub_grid]
    flattened_list = [num for sublist in sub_grid for num in sublist if num > 0 and num < 10]
    # check for distinct value and total sum
    if sum(result) != 45 or len(set(flattened_list)) != 9:
      return

    # handle row, column and diagonal
    sums = [sum(row) for row in sub_grid]
    sums.extend([sum(col) for col in zip(*sub_grid)])
    sums.extend([sum(sub_grid[i][i] for i in range(3)), sum(sub_grid[i][2-i] for i in range(3))])

    if len(set(sums)) == 1:
      self.ans += 1
      return

    return
