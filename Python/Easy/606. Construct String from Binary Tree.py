from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root:
            if root.left and root.right:
                return f"{root.val}({self.tree2str(root.left)})({self.tree2str(root.right)})"
            
            if root.left is None and root.right is None:
                return f"{root.val}"
            
            if root.left is None:
                return f"{root.val}({self.tree2str(root.left)})({self.tree2str(root.right)})"
            
            if root.right is None:
                return f"{root.val}({self.tree2str(root.left)})"
              
        else:
            return ""
            