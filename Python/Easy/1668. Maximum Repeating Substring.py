class Solution:
  def maxRepeating(self, sequence: str, word: str) -> int:
    wordcopy = word
    
    count = 0
    while (wordcopy in sequence):
        count += 1
        wordcopy += word
        
    return count
