class Solution:
  def isCircularSentence(self, sentence: str) -> bool:
    if sentence[0] != sentence[-1]:
      return False
    
    sentence_list = sentence.split()
    check, i = sentence_list[0][-1], 1

    while i < len(sentence_list):
      if sentence_list[i][0] != check:
          return False
        
      check = sentence_list[i][-1]
      i += 1
    
    return True
