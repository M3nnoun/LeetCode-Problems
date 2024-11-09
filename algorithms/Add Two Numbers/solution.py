# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0
        dummy_head = ListNode(0)  # Create a dummy node to simplify handling of head
        current = dummy_head

        # Loop until both lists are done and no remainder is left
        while l1 or l2 or remainder:
            # Get values from each list if they exist
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the new sum and remainder
            total = val1 + val2 + remainder
            remainder = total // 10  # Get the carry
            new_value = total % 10   # Get the digit for the current node
            
            # Create a new node for this digit and attach to the result
            current.next = ListNode(new_value)
            current = current.next
            
            # Move to the next nodes in the input lists if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next  # Return the next of dummy node as the actual head of the output list
