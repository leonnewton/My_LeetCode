__author__ = 'leon'
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root is None:
            return root
        tmp = TreeNode(0)
        tmp = root.right
        root.right = root.left
        root.left = tmp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


class all:
    def test(self,x):
        if x is not None:
            print x.val
            self.test(x.left)
            self.test(x.right)


if __name__ == '__main__':
    f = TreeNode(6)
    d = TreeNode(4)
    e = TreeNode(5)
    b = TreeNode(2)
    c = TreeNode(3)
    c.left = f
    b.left = d
    b.right = e
    a = TreeNode(1)
    a.left = b
    a.right = c
    tmp = Solution()
    node = tmp.invertTree(a)
    test1 = all()
    test1.test(node)