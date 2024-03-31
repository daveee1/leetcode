# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        listar=[]
        listal=[]
        listar.append(root.val)
        listal.append(root.val)
        left=self.f(root.left,p.val,q.val,listal)
        right=self.f(root.right,p.val,q.val,listar)
        #check what is in common
        listac=[]
        for elem in listal:
            if elem in listar:
                listac.append(elem)
        return root


    def f(self,root,p,q,lista):
        if not root:
            return
        if root.val==p or root.val==q:
            print("entrato, ",root.val)
            lista.append(root.val)
            return 
        if self.nodeinsubTree(root.right,p,q):#if right contains at  least one of them 
            print("entrato RIGHT")
            lista.append(root.val)
            self.f(root.right,p,q,lista)  
        if self.nodeinsubTree(root.left,p,q):
            print("entrato LEFT")
            lista.append(root.val)
            self.f(root.left,p,q,lista)


    def nodeinsubTree(self,root,nodetofind,nodetofind2):
        if not root :
            return False
        if root.val==nodetofind or root.val==nodetofind2:
            return True
        left=self.nodeinsubTree(root.left,nodetofind,nodetofind2)
        right=self.nodeinsubTree(root.right,nodetofind,nodetofind2)
        if left or right:
            return True
        return False
