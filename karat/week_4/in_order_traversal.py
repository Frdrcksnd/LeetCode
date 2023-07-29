#https://leetcode.com/problems/binary-tree-preorder-traversal/


def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return
    stack = []
    result = []

    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        result.append(root.val)
        root = root.right

    return result

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