# Task link: https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = ListNode()
        tochka = False
        var = ListNode()
        sum.next = var
        while l1 or l2:
            s = l1.val + l2.val
            if tochka:
                s += 1
            if s < 10:
                tochka = False
            else:
                tochka = True
                s = s % 10
            var.val = s
            l1 = l1.next
            l2 = l2.next
            if l1 is None and l2 is not None:
                l1 = ListNode(0)
            if l2 is None and l1 is not None:
                l2 = ListNode(0)
            var2 = ListNode()
            if l1 is None and l2 is None:
                if tochka:
                    var2 = ListNode(1)
                else:
                    var2 = None
            var.next = var2
            var = var2
        return sum.next