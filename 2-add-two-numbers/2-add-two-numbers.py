# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = node = ListNode() 
        carry = 0
        while l1 or l2:
            #keep looping till both empty
            val1 = 0
            if l1:
                #get curr number
                val1 = l1.val
                l1 = l1.next
            
            val2 = 0
            if l2:
                #get curr number
                val2 = l2.val
                l2 = l2.next
            
            currSum = val1 + val2 + carry
            carry = currSum // 10
            currSum = currSum % 10
            #print(currSum, carry)
            node.val = currSum
            
            prev = node
            node.next = ListNode()
            node = node.next
            
        if carry != 0:
            #print('in')
            node.val = carry
            return l3
        
        if prev.next.val == 0:
            prev.next = None
        
        return l3
            