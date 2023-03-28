# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # START
        # Virtual head
        dummy_head = ListNode(0)
        dummy_head.next = head

        cur = dummy_head
        while (cur.next != None):
            if cur.next.val == val: # 注意是cur.next
                cur.next = cur.next.next
            else:
                cur = cur.next
        
        return dummy_head.next
