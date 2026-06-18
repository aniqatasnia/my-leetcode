# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Iterative solution
# Time O(n) 
# Memory O(1) bcs just using pointers
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # p and q are the pointers I use to traverse linked lists
        # starting at None so head of list currently will be pointing to null
        # when it becomes the tail
        p, q = None, head

        while q:
            next = q.next
            q.next = p
            p = q
            q = next
        
        head = p
        return head

  # Recursive solution
