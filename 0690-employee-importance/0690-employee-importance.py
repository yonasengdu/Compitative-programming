"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.total_importance =  0
        def dfs(employee):
            self.total_importance += employee.importance
            
            if not employee.subordinates:
                
                return 
           
            
            for subordinate_id in employee.subordinates:
                for subordinate in employees:
                    if subordinate.id == subordinate_id:
                        dfs(subordinate)
                   
        for employee in employees:
            if employee.id == id:
                dfs(employee)
                
        return self.total_importance
        
        