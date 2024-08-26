from typing import List, Optional

# Definition for a Node.
class Node:
  def __init__(self, val=None, children=None):
    self.val = val
    self.children = children


class Solution:
  def __init__(self):
    self.answer = []

  def postorder(self, root: Node) -> List[int]:
    self.get_post_traverse(root)

    return self.answer

  def get_post_traverse(self, node: Node) -> None:
    if node != None:
      self.get_post_traverse(self.get_children(node))
      self.answer.append(node.val)

  def get_children(self, node: Node):
    for i in node.children:
        self.get_post_traverse(i)
