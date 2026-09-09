from __future__ import annotations
from typing import Optional,List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        self._traversal(self)
    
    def _traversal(self,root:TreeNode):
        if root is None: return
        print(root.val)
        self._traversal(root.left) if root.left else None
        self._traversal(root.right) if root.right else None
        
    

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.my_recorder = dict()
        for idx,value in enumerate(inorder):
            self.my_recorder[value] = idx
        
        self.preorder,self.inorder = preorder,inorder
        return self.get_tree(0,len(preorder)-1,0,len(inorder)-1)
    
    def get_tree(self,pl:int,pr:int,il:int,ir:int) -> Optional[TreeNode]:
        if pl>pr: return
        
        inorder_root_idx = self.my_recorder[self.preorder[pl]]
        l_len = inorder_root_idx - il
        root = TreeNode(self.preorder[pl])
        root.left = (pl+1,pl+l_len,il,inorder_root_idx-1)
        root.right = (pl+l_len+1,pr,inorder_root_idx+1,ir)
        
        return root

preorder = [3,9,20,15,7];inorder = [9,3,15,20,7];
s = Solution()

root = s.buildTree(preorder=preorder,inorder=inorder)
print(root)