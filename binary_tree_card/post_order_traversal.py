#https://leetcode.com/problems/binary-tree-preorder-traversal/


def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return
    stack = [root]
    result = []

    while stack :
        root = stack.pop()
        result.append(root.val)
        if root.left:
            stack.append(root.left)
        if root.right:
            stack.append(root.right)
    return result.reverse()


def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    result = []
    if not root:
        return

    def helper(root):
        if not root:
            return
        helper(root.left)
        result.append(root.val)
        helper(root.right)

    helper(root)
    return result

"""
Time Complexity -> O(n)
Space Complexity -> O(n)
"""