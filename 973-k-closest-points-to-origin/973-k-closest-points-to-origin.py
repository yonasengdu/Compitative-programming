class Solution:
        def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
                        rep =[]
                        l = []
                        for i in range(len(points)):
                            cordinates = points[i]
                            x = sqrt(cordinates[0]**2 + cordinates[1]**2)
                            rep.append([x,cordinates])
                        rep = sorted(rep,key=lambda rep: rep[0])
                        for i in range(k):
                            l.append(rep[i][1])
                        return l

          

