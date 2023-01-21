class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flat_arr = []
        result = []
        for row in mat:
            flat_arr.extend(row)
        if len(flat_arr) == r*c:
            for ind in range(0,len(flat_arr),c):
                temp = flat_arr[ind:ind+c]
                result.append(temp)
            return result
        else:
            return mat
                