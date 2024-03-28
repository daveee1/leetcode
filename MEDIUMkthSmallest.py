# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lista=[]
        self.f(root,lista)
        lista=sorted(lista)
        i=0
        while lista[i]==-1:
            i+=1
        return lista[i-1+k]
    def f(self,root,list):
        if not root:
            list.append(-1)
            return True
        self.f(root.left,list)
        self.f(root.right,list)
        list.append(root.val)
        return True

