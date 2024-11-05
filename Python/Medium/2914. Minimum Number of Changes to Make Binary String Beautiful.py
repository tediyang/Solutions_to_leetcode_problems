class Solution:
  def minChanges(self, s: str) -> int:
    change, state = 0, None

    for i in s:
      if not state:
        state = i
      elif i == state:
        state = None
      else:
        change += 1
        state = None

    return change
