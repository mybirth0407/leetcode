# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        merged_head = ListNode()
        cur1, cur2 = l1, l2
        merged_tail = merged_head
        while True:
            if cur1 == None:
                while cur2 != None:
                    merged_tail.next = ListNode(cur2.val)
                    merged_tail = merged_tail.next
                    cur2 = cur2.next
                break
            if cur2 == None:
                while cur1 != None:
                    merged_tail.next = ListNode(cur1.val)
                    merged_tail = merged_tail.next
                    cur1 = cur1.next
                break
            if cur1.val <= cur2.val:
                merged_tail.next = ListNode(cur1.val)
                cur1 = cur1.next
            else:
                merged_tail.next = ListNode(cur2.val)
                cur2 = cur2.next
            merged_tail = merged_tail.next

        merged_head = merged_head.next
        return merged_head