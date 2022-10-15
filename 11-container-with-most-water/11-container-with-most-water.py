class Solution:
    def maxArea(self, height: List[int]) -> int:
        pointer1 = 0
        pointer2 = len(height)-1
        area = 0
        while pointer1 < pointer2:
            area = max(area, (pointer2-pointer1)*min(height[pointer1],height[pointer2]))
            if height[pointer1] < height[pointer2]:
                pointer1 +=1
            else:
                pointer2 -= 1
        return area
            
        