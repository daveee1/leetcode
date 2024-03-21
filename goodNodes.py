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
        lista=[]
        lista.append(root.val)
        ans=self.ff(root,lista,count)
        return ans
        
        
    def ff(self,node, lista , count):
        if not node:
            return 0
        big=max(lista)
        lista.append(node.val)
        r1=self.ff(node.left,lista,count)
        r2=self.ff(node.right,lista,count)
        count=r2+r1
        if node.val>=big:
            count+=1
        lista.remove(node.val)
        return count
        

        
