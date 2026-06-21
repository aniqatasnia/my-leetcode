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
# Time O(n)
# Memory O(n)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            
            return None 
        if not head.next:

            return head
        
        newhead = self.reverseList(head.next)
        revtail = head.next
        revtail.next = head
        head.next = None

        return newhead

# more elegantly written version of above recursive solution:
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newhead = head
        if head.next:
            newhead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        
        return newhead

# Recursive solution explanation below:
# if not head --> edge case: empty list, return None
# newhead = head --> eventually we'll return just this current node if there's nothing after it / consider the current head (node) as the new one if it's the end of the original list (i.e., if the code block/branch for additional nodes present in the list underneath doesn't run)
# if head.next --> we're checking if there's actually more nodes in the list or if we're at the end 
# if there is more --> do the things to reverse the linked list up until this point and include this node (changing the next ptr of the following node in the original list to point to head/"me" instead with `head.next.next = head`)
# whether we were at the end of the original list anyways or there was more and we reversed it up to this point, set the next ptr of the current node to null (marking the end of the reversed list or at least the reversed portion) and returnthe head of the newly reversed list (if it was only a portion of the original list, then we're returning the reversed list for this call). The goal is to eventually pop out of the recursion stack to where newhead = head and head.next doesn't exist because we're at the end and we're done.
