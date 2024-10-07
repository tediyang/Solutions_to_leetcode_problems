class Solution:
  def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
    sentence1 = sentence1.split(' ')
    sentence2 = sentence2.split(' ')

    if len(sentence1) > len(sentence2):
      sentence1, sentence2 = sentence2, sentence1

    pick_left, pick_right = 0, len(sentence1) - 1
    check_left, check_right = 0, len(sentence2) - 1

    while pick_left <= pick_right:
      if sentence1[pick_left] == sentence2[check_left]:
        pick_left += 1
        check_left += 1
  
      elif sentence1[pick_right] == sentence2[check_right]:
        pick_right -= 1
        check_right -= 1

      else:
        break
    
    return pick_left > pick_right
