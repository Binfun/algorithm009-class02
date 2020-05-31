# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        l = []
        l.extend(self.inorderTraversal(root.left))
        l.append(root.val)
        l.extend(self.inorderTraversal(root.right))
        return l

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            top = stack.pop() #此时左子树遍历完成
            res.append(top.val)  #将父节点加入列表
            cur = top.right #遍历右子树
        return res

