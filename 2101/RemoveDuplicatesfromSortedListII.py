# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        elif head.next == None:
            return head
        
        removed_list = ListNode()
        removed_tail = removed_list
        cur = head.next
        prev = head
        remove_set = set()
        while cur != None:
            if prev.val != cur.val:
                if prev.val not in remove_set:
                    removed_tail.next = ListNode(prev.val)
                    removed_tail = removed_tail.next
            else:
                remove_set.add(prev.val)
            prev = cur
            cur = cur.next
        if prev.val not in remove_set:
            removed_tail.next = ListNode(prev.val)
            removed_tail = removed_tail.next
        removed_list = removed_list.next
        return removed_list