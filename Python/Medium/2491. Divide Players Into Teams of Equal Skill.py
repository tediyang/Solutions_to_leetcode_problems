from typing import List

class Solution:
  def dividePlayers(self, skill: List[int]) -> int:
    length = len(skill)
    if len(skill) == 2:
      return skill[0] * skill[1]

    summed = sum(skill)
    if summed % (length/2) != 0:
      return -1

    number = summed / (length/2)
    skill.sort()
    left = 0
    right = length - 1
    answer = 0

    while left < right:
      if skill[left] + skill[right] != number:
        return -1

      answer += skill[left] * skill[right]
      left += 1
      right -= 1

    return answer
