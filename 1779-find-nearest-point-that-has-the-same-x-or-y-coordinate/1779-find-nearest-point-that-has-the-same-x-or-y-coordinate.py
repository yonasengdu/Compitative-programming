class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        manhattan_distance = 10**6
        index = -1
        for i in range(len(points)):
            point_x = points[i][0]
            point_y = points[i][1]
            if point_x == x and point_y == y:
                return i
            elif point_x == x:
                temp_manhattan_distance = abs(y-point_y)
                if temp_manhattan_distance < manhattan_distance:
                    manhattan_distance = temp_manhattan_distance
                    index = i
            elif point_y == y:
                    temp_manhattan_distance = abs(x-point_x) 
                    if temp_manhattan_distance < manhattan_distance:
                            manhattan_distance = temp_manhattan_distance
                            index = i
        if index == -1:
            return -1
        else:
            return index
     
                
            
            
        