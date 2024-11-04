class Solution:
  def compressedString(self, word: str) -> str:
    comp = ''
    char = word[0]
    count = 0

    for i in word:
      if i == char and count == 9:
        comp += str(count) + char
        count = 1
      elif i == char:
        count += 1
      else:
        comp += str(count) + char
        count = 1
        char = i
    
    comp += str(count) + char #handle last char
    
    return comp
