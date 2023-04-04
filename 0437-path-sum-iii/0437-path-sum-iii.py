# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.total = 0
        self.lookup =  defaultdict(int)
        self.lookup[targetSum] += 1 
        def dfs(root,curr_sum):
            if not root:
                return 
            curr_sum += root.val
            self.total += self.lookup[curr_sum]
            self.lookup[curr_sum + targetSum]  += 1

            dfs(root.left,curr_sum)
            dfs(root.right,curr_sum)

            self.lookup[curr_sum + targetSum] -= 1
            
        dfs(root,0)

        return self.total
        