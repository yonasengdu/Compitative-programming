class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.inheritance = defaultdict(list)
        self.inheritance[self.kingName] = []
        self.dead = set()
        

    def birth(self, parentName: str, childName: str) -> None:
        self.inheritance[parentName].append(childName)
        
    def death(self, name: str) -> None:
        self.dead.add(name)
        
    def getInheritanceOrder(self) -> List[str]:
        inheritance_order = []
        
        visited = set()
        def dfs(parent):
            inheritance_order.append(parent)
            
            for nigh in self.inheritance[parent]:
                if nigh not in visited:
                    visited.add(nigh)
                    dfs(nigh)
                    
            return inheritance_order
        dfs(self.kingName)
        
        diff = 0
        for ind in range(len(inheritance_order)):
            if inheritance_order[ind - diff] in self.dead:
                inheritance_order.pop(ind - diff)
                diff += 1
                
        return inheritance_order
        
        
     
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()