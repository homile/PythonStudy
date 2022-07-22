# Binary Tree Preorder Traversal
# 링크:

# 문제풀이(1)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        # TreeNode{val: 1, left: None, right: TreeNode{val:2, left: TreeNode{val:3, left:None, right:None}, right: None}}
        # right부터 순회?
        # left가 none이면 right 순회
        # 아니라면 left순회

        def dfs(root):
            if root is not None:
                dfs(root.left)
                result.append(root.val)
                dfs(root.right)
                
        dfs(root)
        return result
