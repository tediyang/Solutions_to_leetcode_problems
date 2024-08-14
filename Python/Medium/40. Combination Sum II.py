from typing import List

class Solution:
  def __init__(self):
    self.combinations = []
    self.state = []

  def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    filtered_candidates = filter(lambda x: x <= target, candidates)
    sorted_candidates = sorted(filtered_candidates)

    self.combine(sorted_candidates, 0, target)

    return self.combinations

  def combine(self, candidates: List[int], start, target):
    if target == 0:
      self.combinations.append(self.state.copy())
      return True

    elif target < 0:
      return False

    for num in range(start, len(candidates)):
      if num > start and candidates[num] == candidates[num - 1]:
        continue

      self.state.append(candidates[num])
      active = self.combine(candidates, num + 1, target - candidates[num])
      # remove the recently added data for backtracking
      self.state.pop()
      if active == True or active == False:
        break

    return
