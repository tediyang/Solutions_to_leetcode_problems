# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        tree = TreeNode()
        a = root.val
        left = root.left
        right = root.right
        if root:
            if left is None and right is None:
                return True
            
            elif right is None: 
                if (a == left.val):
                    return self.isUnivalTree(left)
                else:
                    return False
            elif left is None:
                if (a == right.val):
                    return self.isUnivalTree(right)
                else:
                    return False
            
            elif a == left.val == right.val:
                l = self.isUnivalTree(left)
                r = self.isUnivalTree(right)
                return (l and r)
            
            else:
                return False
        
        return True
            
        
        
        
        