# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        i = 0

        curr = head

        while curr:
            curr = curr.next
            i += 1
        print(i)
        
        if i == 1 and n == i:
            return None

        curr2 = result = head
        location = i - n

        if location == 0:
            return head.next
        print(location)
        j = 0

        while curr2:
            
            if j == location - 1:
                if curr2.next.next:
                    curr2.next = curr2.next.next
                else:
                    curr2.next = None
            j += 1
            curr2 = curr2.next
        
        return head

        


        