from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = dummy = ListNode()
        remain = 0
        
        while l1 or l2:
            v1, v2 = 0, 0
            
            if l1:
                v1, l1 = l1.val, l1.next
            if l2:
                v2, l2 = l2.val, l2.next
            
            sum_ = v1 + v2 + remain
            res.next = ListNode(sum_ % 10)
            res = res.next
            remain = sum_ // 10
        
        if remain:
            res.next = ListNode(remain)
        
        return dummy.next