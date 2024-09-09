from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
  def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
    answer = [[-1] * n for _ in range(m)]
    i, j, k = 0, 0, 0
    move  = 'right'

    while head != None:
      if n == 1:
        answer[i] = [head.val]
        i += 1
        head = head.next
        continue

      answer[i][j] = head.val

      if move == 'right':
        j += 1
        if j + 1 >= n - k:
            move = 'down'
      elif move == 'down':
        i += 1
        if i + 1 >= m - k:
            move = 'left'

      elif move == 'left':
        j -= 1
        if j <= k:
            move = 'up'

      else:
        i -= 1
        if i - 1 <= k:
            move = 'right'
            k += 1

      head = head.next
          
    return answer
