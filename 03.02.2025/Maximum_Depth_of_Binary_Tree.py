# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root==None:
            return 0
        lefttree= self.maxDepth( root.left)
        righttree=self.maxDepth( root.right)
        return (max(lefttree,righttree)+1)

        

            
        
        


        
