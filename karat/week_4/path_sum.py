#https://leetcode.com/problems/path-sum/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def check(root, targetSum, val):
            if not root:
                return
            curr = root.val + val
            if curr == targetSum and not root.left and not root.right:
                return True
            return check(root.left, targetSum, curr) or check(root.right, targetSum. curr)
        if check(root, targetSum, 0):
            return True
        else:
            return False

"""
Time Complexity -> O(n)
Space Complexity -> O(n)
"""