# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next:
            return False
        curr = head
        faster_curr = head


        while faster_curr and faster_curr.next:
            curr = curr.next
            faster_curr = faster_curr.next.next
            if curr == faster_curr:
                return True
            
        return False
        