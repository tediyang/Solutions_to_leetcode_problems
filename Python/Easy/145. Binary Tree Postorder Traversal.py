from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right


class Solution:
  def __init__(self):
    self.answer = []

  def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    self.get_post_traverse(root)
    return self.answer

  def get_post_traverse(self, node: TreeNode) -> None:
    if node != None:
      self.postorderTraversal(self.get_left(node))
      self.postorderTraversal(self.get_right(node))
      self.answer.append(node.val)

  def get_right(self, node):
    return node.right

  def get_left(self, node):
    return node.left

  def get_node_value(self, node):
    return node.val
