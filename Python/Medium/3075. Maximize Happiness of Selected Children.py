from typing import List
import heapq

class Solution:
  def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
    # convert to heap
    max_heap = [-h for h in happiness] # heapq uses minimum, so convert to negative to get maximum
    heapq.heapify(max_heap)
    
    reduction = 0
    total = 0

    for _ in range(k):
      # Get the maximum value (negate to get original value)
      happy = -heapq.heappop(max_heap) - reduction # heappop removes the smallest item from the heap.
      total += 0 if happy < 0 else happy
  
      reduction += 1

    return total
