class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        middle = []
        right = []
        
        for num in nums:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                middle.append(num)
        return left + middle + right