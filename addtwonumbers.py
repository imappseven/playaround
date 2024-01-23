from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp_head = ListNode()
        current = temp_head
        regroup = 0

        while l1 or l2 or regroup:
            # Get values from current nodes or 0 if node is None
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # Calculate sum and carry
            total = x + y + regroup
            regroup, digit = divmod(total, 10)

            # Create a new node with the result digit
            current.next = ListNode(digit)
            current = current.next

            # Move to the next nodes if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return temp_head.next

# Example usage:
# Create linked lists: 0 -> 8 -> 6 and 6 -> 7 -> 8
l1 = ListNode(0, ListNode(8, ListNode(6)))
l2 = ListNode(6, ListNode(7, ListNode(8)))

solution = Solution()
result_list = solution.addTwoNumbers(l1, l2)

# Print the result_list values
while result_list:
    print(result_list.val, end=" ")
    result_list = result_list.next