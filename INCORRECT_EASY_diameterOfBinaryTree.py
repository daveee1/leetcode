# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #devo passare il valore della profondita maggiore
        if not root: 
            return 0
        dl=self.f(root.left)
        dr=self.f(root.right)
        print(dl,dr)
        return dl+dr

    def f(self,root):
        if not root:
            return 0
        dl=self.f(root.left)
        dr=self.f(root.right)
        if dl==dr:
            return dl+1
        return max(dl,dr)+1
        
