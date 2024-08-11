from collections import Counter


class Solution:
  def minimumPushes(self, word: str) -> int:
    count = Counter(word)
    mini = 0
    mapped = 8
    times = 1

    sorted_distinct = sorted(list(count.values()), reverse=True)
    length = len(sorted_distinct)
    
    diff = length - (mapped * times)
    
    while (diff >= 0):
        mini += sum(sorted_distinct[mapped * (times - 1): mapped * (times)]) * times
            
        times += 1
        diff = length - (mapped * times)
    
    mini += sum(sorted_distinct[mapped * (times - 1):]) * times
        
    return mini
