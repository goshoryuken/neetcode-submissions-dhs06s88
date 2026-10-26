# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #1. find the middle of the list using tort nd hare

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #slow.next should now have the middle node
        curr = slow.next 
        slow.next = None
        prev = None

        #2. reverse second half of linked list
        while curr:
            temp = curr.next

            curr.next = prev
            prev = curr
            

            curr = temp
        
        #3. build new list in alternating order

        first = head
        second = prev

        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
        