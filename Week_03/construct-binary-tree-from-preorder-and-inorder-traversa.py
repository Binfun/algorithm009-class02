class Solution:
	def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
		if len(inorder) == 0:
			return None
		# 前序遍历第一个值为根节点
		root = TreeNode(preorder[0])
		# 因为没有重复元素，所以可以直接根据值来查找根节点在中序遍历中的位置
		mid = inorder.index(preorder[0])
		root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
		root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
		return root