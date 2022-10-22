# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def __init__(self):
        self.ans = []
    
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        small = []
        if root:
            if type(root) != list:
                self.ans.append([root.val])
            
            if type(root) == list:
                for i in root:
                    if i is not None:
                        small.append(i.val)
                self.ans.append(small)
            
                child = [i.children for i in root if i is not None]
            
                if child:
                    self.levelOrder([j for i in child for j in i])
            
            else:
                self.levelOrder(root.children)
                
        return self.ans