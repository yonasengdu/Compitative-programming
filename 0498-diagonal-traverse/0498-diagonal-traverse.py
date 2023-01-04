class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        val = {}
        ans = []
        for row_index in range(len(mat)):
            row_arr = mat[row_index]
            for col_index in range(len(row_arr)):
                index_sum = row_index + col_index
                col_val = row_arr[col_index]
                if index_sum in val:
                    val[index_sum].append(col_val)
                else:
                    val[index_sum] = [col_val]
        for key,val in val.items():
            if key %2 == 0:
                ans += reversed(val)
            else:
                ans += val
                
        return ans
        