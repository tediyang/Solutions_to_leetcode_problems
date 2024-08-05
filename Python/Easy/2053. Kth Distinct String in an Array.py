from collections import Counter
from typing import List


class Solution:
  def kthDistinct(self, arr: List[str], k: int) -> str:
    try:
      count = Counter(arr) 

      distinct = [key for key, value in count.items() if value == 1]
      return distinct[k -1]
      
    except IndexError:
      return ""
