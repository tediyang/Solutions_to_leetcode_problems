class Solution:
  def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
    sentence1 = sentence1.split(' ')
    sentence2 = sentence2.split(' ')

    if len(sentence1) > len(sentence2):
      pick = sentence2
      check = sentence1
    else:
      pick = sentence1
      check = sentence2

    while len(pick) > 0:
      if pick[0] == check[0]:
        pick.pop(0)
        check.pop(0)
  
      elif pick[-1] == check[-1]:
        pick.pop()
        check.pop()

      else:
        break

    if len(pick) == 0:
      return True
    
    return False
