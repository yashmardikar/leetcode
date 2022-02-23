# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        prev = None
        curr = head
        while curr:
            #save next node addr first
            nxt = curr.next
            #update the curr nodes next as we backup up
            curr.next = prev
            prev = curr
            curr = nxt
        head = prev
        return head