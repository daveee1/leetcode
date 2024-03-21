    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def goodNodes(self, root: TreeNode) -> int:
            if not root:
                return 0
            count=1#consider root
            ans=self.ff(root,root.val)
            return ans        
        def ff(self,node, big):
            if not node:
                return 0
            big=max(node.val,big)
            r1=self.ff(node.left,big)
            r2=self.ff(node.right,big)
            sum=r2+r1
            if node.val>=big:
                sum+=1
            return sum
