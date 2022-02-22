# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1, node2 = l1, l2
        head = new_node = ListNode()
        carryOver = 0
        while node1 or node2:
            val1, val2 = 0, 0
            if node1:
                val1 = node1.val
                node1 = node1.next
            if node2:
                val2 = node2.val
                node2 = node2.next
            val = val1 + val2 + carryOver
            carryOver = val // 10
            val = val % 10
            new_node.val = val
            if node1 or node2:
                new_node.next = ListNode()
                new_node = new_node.next
            elif carryOver:
                new_node.next = ListNode()
                new_node.next.val = carryOver
                new_node.next.next = None
            else:
                new_node.next = None
        return head