"""
# Definition for a Node.
class Node(object):
	def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        arr = []

        def dfs(node):
            if node is None:
                return

            for child in node.children:
                dfs(child)

            arr.append(node.val)

        dfs(root)
        return arr

