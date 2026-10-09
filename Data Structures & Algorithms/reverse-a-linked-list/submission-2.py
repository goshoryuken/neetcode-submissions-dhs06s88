# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev, curr = None, head

        while curr:
            #temp = 1
            temp = curr.next
            # None <- 0
            curr.next = prev
            prev = curr
            #None <- 0 | 1 2 3
            curr = temp


        return prev
        