class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        order = []
        graph = defaultdict(list)
        ind = defaultdict(int)
        
        
        for idx,sub_arr in enumerate(ingredients) :
            for rec in sub_arr:
                graph[rec].append(recipes[idx])
                ind[recipes[idx]] += 1
                
                
        
        queue = deque()
        
        for init in supplies:
            queue.append(init)
        
        supplies = set(supplies)
        while queue:
            
            curr = queue.pop()
            
            if curr not in supplies:
                order.append(curr)
            
            for child in graph[curr]:
                ind[child] -= 1
                
                if not ind[child]:
                    queue.append(child)
                    
                    
        return order
        