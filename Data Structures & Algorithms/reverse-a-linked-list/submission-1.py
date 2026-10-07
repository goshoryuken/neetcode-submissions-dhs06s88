# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, current = None, head

        while current:
            #save the 1
            temp = current.next
            #None <- 0
            current.next = prev
            prev = current

            #move on to 1
            current = temp


        return prev


        