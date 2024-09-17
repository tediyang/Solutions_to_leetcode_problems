from collections import Counter
from typing import List


class Solution:
  def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
    sentence = (s1 + ' ' + s2).split(' ')
    count = Counter(sentence)

    return [key for key, val in count.items() if val == 1]
