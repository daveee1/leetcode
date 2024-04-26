# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root.right and not root.left:
            return 1
        listal=[]
        listar=[]
        listal.append(root.val)
        listar.append(root.val)
        ans=[0]
        ans[0]=1
        self.f(root.left,listal,ans)
        self.f(root.right,listar,ans)
        return ans[0]


    def f(self,root,list,ans):
        if not root:
            return
        if root.val>=list[-1]:
            list.append(root.val)
            ans[0]+=1
            
        self.f(root.left,list,ans)
        self.f(root.right,list,ans)
        
        if root.val==list[-1]:
            list.pop()
        return
