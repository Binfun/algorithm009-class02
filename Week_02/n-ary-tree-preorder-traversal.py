class Solution(object):
    def preorder_iterative(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        traversal = []
        stack = [root]
        while stack:
            cur = stack.pop()
            traversal.append(cur.val)
            stack.extend(reversed(cur.children))
        return traversal

    def preorder_recursive(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        traversal = [root.val]
        for child in root.children:
            traversal.extend(self.preorder(child))
        return traversal
    