# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: 
            return True
        if not root.left and not root.right:
            return True
        valore=root.val
        subtreer=self.f(root.right,valore,0)
        subtreel=self.f(root.left,valore,1)
        
        if subtreel==False or subtreer==False:
            return False
        elif not root.left or not root.right:
            if not root.left:
                if root.right.val>root.val:
                    return True
                else:
                    return False
            else:
                if root.left.val<root.val:
                    return True
                else:
                    return False
        elif root.right.val<=root.val or root.left.val>=root.val:
            return False
        return True
        
    def f(self,root,valprevroot,num):
        if not root:
            return True
        if not root.left and not root.right:
            return True
        
        subtreer=self.f(root.right,root.val,0)
        subtreel=self.f(root.left,root.val,1)

        if subtreel==False or subtreer==False:
            return False

        if num==0:
            #ogni node deve essere di val > di valprevroot
            node=root
            while node:
                print(node.val)
                if node.val<=valprevroot:
                    return False
                node=node.right
            node=root
            while node:
                if node.val<=valprevroot:
                    return False
                node=node.left
        else:
            node=root
            while node:
                if node.val>=valprevroot:
                    return False
                node=node.right
            node=root
            while node:
                if node.val>=valprevroot:
                    return False
                node=node.left
        if not root.left or not root.right:
            if not root.left:
                if root.right.val>root.val:
                    return True
                else:
                    return False
            else:
                if root.left.val<root.val:
                    return True
                else:
                    return False
        elif root.right.val<=root.val or root.left.val>=root.val:
            return False
        return True
