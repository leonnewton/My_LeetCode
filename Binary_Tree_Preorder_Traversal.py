class Stack:
    def __init__(self):
        self.stack=[]

    def pop(self):
        return self.stack.pop()

    def push(self,obj):
        self.stack.append(obj)

    def length(self):
        return len(self.stack)
        
        
class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        
        s=Stack()
        result=[]

        if root is None:
            return result
        else:
            while (not root is None) or s.length()!=0:
                while not root is None:
                    result.append(root.val)
                    s.push(root)
                    root = root.left

                root = s.pop()
                root = root.right


        return result
        