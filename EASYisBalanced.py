# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        dl=self.isBalanced(root.right)
        dr=self.isBalanced(root.left)
        if abs(dl-dr)>1 or dl==False or dr==False:
            return False
        return max(dl,dr)+1
        
