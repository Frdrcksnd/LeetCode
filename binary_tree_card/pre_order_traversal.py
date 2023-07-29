#https://leetcode.com/problems/binary-tree-preorder-traversal/


def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return
    stack = []
    result = []
    stack.append(root)

    while stack:
        curr = stack.pop()
        result.append(curr.val)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    return result

def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    result = []
    if not root:
        return

    def helper(root):
        if not root:
            return
        result.append(root.val)
        helper(root.left)
        helper(root.right)

    helper(root)
    return result

"""
Time Complexity -> O(n)
Space Complexity -> O(n)
"""