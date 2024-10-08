# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # reversed_linked_list = []
        if not head or not head.next:
            return head
        
        
        reverse = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return reverse

        