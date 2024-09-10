from typing import Optional
import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head

        temp = head
        while head.next:
            min_num = math.gcd(head.val, head.next.val)
            new = ListNode(min_num)
            new.next = head.next
            head.next = new

            head = head.next.next

        return temp

