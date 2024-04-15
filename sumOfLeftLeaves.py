# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  
        ans=[0]
        self.f(root,ans,0)
        return ans[0]
        
        
    def f(self,root,ans,i):    
        if not root:
            return 0
        if not root.right and not root.left:
            if i==1:
                ans[0]+=root.val
            return root.val
        self.f(root.left,ans,1)
        self.f(root.right,ans,0)
        return 
        
