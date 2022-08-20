class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
                intervals.sort()
                merged = [intervals[0]]
                for i,j in  intervals[1:] :
                    if merged[-1][1]>=i:
                        merged[-1][1] = max(merged[-1][1],j)
                    else: merged.append([i,j])

                return merged


