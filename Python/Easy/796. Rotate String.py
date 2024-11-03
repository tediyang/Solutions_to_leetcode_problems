class Solution:
  def rotateString(self, s: str, goal: str) -> bool:
    shift = ""
    i = 0

    while i < len(s):
      if s[i] == goal[0] and (s[i:] + shift) == goal:
        return True
      shift += s[i]
      i += 1
      
    return False
