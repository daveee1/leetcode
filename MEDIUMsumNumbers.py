# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        lista=[root.val]
        ans=[0]
        l=self.f(root.left,lista,ans)
        r=self.f(root.right,lista,ans)
        if l==-1 and r==-1:
            return root.val
        return ans[0]
        
    def f (self,root,lista,ans):
        if not root:
            return -1
        lista.append(root.val)
        l=self.f(root.left,lista,ans)
        r=self.f(root.right,lista,ans)
        if l==-1 and r==-1:
            number=0
            #lets determine the number
            i=len(lista)-1
            for elem in lista:
               number+=elem*10**(i)
               i-=1
            ans[0]+=number
        #lista.remove(root.val) cant use it because destroys the order of the array
        lista.pop()
            
