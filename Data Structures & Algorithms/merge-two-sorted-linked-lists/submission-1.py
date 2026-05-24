from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        sorted_list = ListNode(0)
        head = sorted_list
        while list1 or list2:
            if sorted_list.next:
                sorted_list = sorted_list.next
            if not list1:
                if list2:
                    # sorted_list.next = ListNode(list2.val)
                    sorted_list.next = list2
                    list2 = list2.next
                    continue
            if not list2:
                if list1:
                    # sorted_list.next = ListNode(list1.val)
                    sorted_list.next = list1
                    list1 = list1.next
                    continue
            if list1.val <= list2.val:
                # sorted_list.next = ListNode(list1.val)
                sorted_list.next = list1
                list1 = list1.next
            else:
                # sorted_list.next = ListNode(list2.val)
                sorted_list.next = list2
                list2 = list2.next
        return head.next if head else head


list1 = []

list1 = ListNode(1)
list1.next = ListNode(3)
list1.next.next = ListNode(4)
list1.next.next.next = ListNode(5)

list2 = []

list2 = ListNode(1)
list2.next = ListNode(2)
list2.next.next = ListNode(4)
list2.next.next.next = ListNode(7)

solution = Solution()
sorted_list = solution.mergeTwoLists(list1, list2)
while sorted_list:
    print(sorted_list.val)
    sorted_list = sorted_list.next
