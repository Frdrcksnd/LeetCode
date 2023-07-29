#https://leetcode.com/problems/count-univalue-subtrees/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        result = 0

        def dfs(root, parent):
            nonlocal result
            if not root:
                return True
            left = dfs(root.left, root)
            right = dfs(root.right, root)
            if not left or not right:
                return False
            result += 1

            return root.val == parent.val
        dfs(root, 0)
        return result


"""
Time Complexity -> O(n)
Space Complexity -> O(n)
"""