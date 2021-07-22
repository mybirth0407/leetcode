from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q = deque()
        q.append(cloned)
        
        while True:
            search = q.popleft()
            if target.val == search.val:
                return search
                
            if search.left != None:
                q.append(search.left)
            if search.right != None:
                q.append(search.right)