# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Double pointer
        pre = None
        cur = head
        while(cur != None):
            temp = cur.next
            cur.next = pre
            # move 1 element forward
            pre = cur
            cur = temp 
        
        return pre
