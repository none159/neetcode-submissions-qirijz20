# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res_1 = []
        res_2 = []
        def dfs(root,res):
            if not root:
                res.append(root)
                return None
            res.append(root.val)
            left = dfs(root.left,res)
            right = dfs(root.right,res)
        
        dfs(p,res_1)
        dfs(q,res_2)
        print(res_1)
        print(res_2)
        if res_1 != res_2:
            return False

        return True
