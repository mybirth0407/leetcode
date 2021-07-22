# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def _node2num(l):
            num = ''
            cur = l
            while cur != None:
                num = str(cur.val) + num
                cur = cur.next

            return int(num)

        def _num2node(n):
            node = ListNode(n[-1])
            cur = node
            for i in range(len(n)-2, -1, -1):
                cur.next = ListNode(n[i])
                cur = cur.next

            return node

        l1num = _node2num(l1)
        l2num = _node2num(l2)

        ansnum = str(l1num + l2num)
        ans = _num2node(ansnum)

        return ans
