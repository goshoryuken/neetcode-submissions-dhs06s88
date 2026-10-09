# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        tail = dummy

        #while both lists still have nodes left
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1 #attach smaller node
                list1 = list1.next #move list forward
            else:
                tail.next = list2 #attach smaller node
                list2 = list2.next # move list forward
            tail = tail.next #move tail onto node js attached
        
        tail.next = list1 or list2 #attach whatever's left
        return dummy.next #skip throwaway node added
        
        