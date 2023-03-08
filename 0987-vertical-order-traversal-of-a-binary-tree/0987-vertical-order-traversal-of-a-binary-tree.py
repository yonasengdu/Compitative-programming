# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        lst = [[(0,0),root]]
        
        temp = []
        ans =  [[(0,0),root.val]]
        i = 0
        
        while lst:
            idx,node = lst[i]
            
            if node.right:
                x , y = idx[0] + 1 , idx[1] + 1
                temp.append([(x,y),node.right])
            if node.left:
                x , y = idx[0] + 1 , idx[1] - 1
                temp.append([(x,y),node.left])
                
            if i == len(lst) - 1:
                if temp:
                    for t in temp:
                        ind,node = t
                        ans.append([(t[0][1],t[0][0]),t[1].val])
                lst = temp
                temp = []
                i = 0
            else:
                i += 1
                
        ans.sort()
        
        temp_result = {}
        
       
    
        
        for col in ans:
            if col[0][0] in temp_result:
                temp_result[col[0][0]].append(col[1])
            else:
                temp_result[col[0][0]] = [col[1]]
      
                
        result = [x for x in temp_result.values()]

        return result