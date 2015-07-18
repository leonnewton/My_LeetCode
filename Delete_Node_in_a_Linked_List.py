# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):
         if node.next is not None:
             node.val = node.next.val
             node.next = node.next.next



if  __name__ == '__main__':
    e = ListNode(5)

    d = ListNode(4)
    #d.next = e
    c = ListNode(3)
    c.next = d
    b = ListNode(2)
    b.next = c
    a = ListNode(1)
    a.next = b
    node = a
    s = Solution()
    s.deleteNode(b)
    while not node is  None:
        print node.val
        node = node.next