# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        # a sentinel head.
        dummy_head = ListNode(0)
        dummy_head.next = head
        # head is an anchor.
        # start from the head's next.
        current = head.next
        # process the whole list.
        while current:
            # remember the real next
            real_next = current.next
            # remove current from the original list
            head.next = current.next
            # insert it next to dummy_head
            current.next = dummy_head.next
            dummy_head.next = current
            # advance
            current = real_next
        return dummy_head.next 
       