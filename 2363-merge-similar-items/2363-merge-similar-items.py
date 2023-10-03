class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        merged = defaultdict(int)
        
        for value,weight in items1:
            merged[value] += weight
            
    
        for value,weight in items2:
            print(value,weight)
            merged[value] += weight
            
        
            
        return sorted([[value,weight] for value,weight in merged.items()])
        